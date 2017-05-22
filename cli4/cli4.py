#!/usr/bin/env python
"""Cloudflare API via command line"""

import sys
import re
import getopt
import json
try:
    import yaml
except ImportError:
    yaml = None

from . import converters

import CloudFlare

def dump_commands(cf):
    """dump a tree of all the known API commands"""
    w = cf.api_list()
    sys.stdout.write('\n'.join(w) + '\n')

def cli4(args):
    """Cloudflare API via command line"""

    verbose = False
    output = 'json'
    raw = False
    dump = False
    method = 'GET'

    usage = ('usage: cli4 '
             + '[-V|--version] [-h|--help] [-v|--verbose] [-q|--quiet] [-j|--json] [-y|--yaml] '
             + '[-r|--raw] '
             + '[-d|--dump] '
             + '[--get|--patch|--post|--put|--delete] '
             + '[item=value ...] '
             + '/command...')

    try:
        opts, args = getopt.getopt(args,
                                   'VhvqjyrdGPOUD',
                                   [
                                       'version',
                                       'help', 'verbose', 'quiet', 'json', 'yaml',
                                       'raw',
                                       'dump',
                                       'get', 'patch', 'post', 'put', 'delete'
                                   ])
    except getopt.GetoptError:
        exit(usage)
    for opt, arg in opts:
        if opt in ('-V', '--version'):
            exit('Cloudflare library version: %s' % (CloudFlare.__version__))
        if opt in ('-h', '--help'):
            exit(usage)
        elif opt in ('-v', '--verbose'):
            verbose = True
        elif opt in ('-q', '--quiet'):
            output = None
        elif opt in ('-j', '--json'):
            output = 'json'
        elif opt in ('-y', '--yaml'):
            if yaml is None:
                exit('cli4: install yaml support')
            output = 'yaml'
        elif opt in ('-r', '--raw'):
            raw = True
        elif opt in ('-d', '--dump'):
            dump = True
        elif opt in ('-G', '--get'):
            method = 'GET'
        elif opt in ('-P', '--patch'):
            method = 'PATCH'
        elif opt in ('-O', '--post'):
            method = 'POST'
        elif opt in ('-U', '--put'):
            method = 'PUT'
        elif opt in ('-D', '--delete'):
            method = 'DELETE'

    digits_only = re.compile('^-?[0-9]+$')
    floats_only = re.compile('^-?[0-9.]+$')

    # next grab the params. These are in the form of tag=value
    params = None
    while len(args) > 0 and '=' in args[0]:
        tag_string, value_string = args.pop(0).split('=', 1)
        if value_string == 'true':
            value = True
        elif value_string == 'false':
            value = False
        elif value_string == '':
            value = None
        elif value_string[0] is '=' and value_string[1:] == '':
            exit('cli4: %s== - no number value passed' % (tag_string))
        elif value_string[0] is '=' and digits_only.match(value_string[1:]):
            value = int(value_string[1:])
        elif value_string[0] is '=' and floats_only.match(value_string[1:]):
            value = float(value_string[1:])
        elif value_string[0] is '=':
            exit('cli4: %s== - invalid number value passed' % (tag_string))
        elif value_string[0] in '[{' and value_string[-1] in '}]':
            # a json structure - used in pagerules
            try:
                #value = json.loads(value) - changed to yaml code to remove unicode string issues
                if yaml is None:
                    exit('cli4: install yaml support')
                value = yaml.safe_load(value_string)
            except ValueError:
                exit('cli4: %s="%s" - can\'t parse json value' % (tag_string, value_string))
        else:
            value = value_string
        if tag_string == '':
            # There's no tag; it's just an unnamed list
            if params is None:
                params = []
            try:
                params.append(value)
            except AttributeError:
                exit('cli4: %s=%s - param error. Can\'t mix unnamed and named list' %
                     (tag_string, value_string))
        else:
            if params is None:
                params = {}
            tag = tag_string
            try:
                params[tag] = value
            except TypeError:
                exit('cli4: %s=%s - param error. Can\'t mix unnamed and named list' %
                     (tag_string, value_string))

    if dump:
        cf = CloudFlare.CloudFlare()
        dump_commands(cf)
        exit(0)

    # what's left is the command itself
    if len(args) != 1:
        exit(usage)

    command = args[0]
    # remove leading and trailing /'s
    if command[0] == '/':
        command = command[1:]
    if command[-1] == '/':
        command = command[:-1]

    # break down command into it's seperate pieces
    # these are then checked against the Cloudflare class
    # to confirm there is a method that matches
    parts = command.split('/')

    cmd = []
    identifier1 = None
    identifier2 = None
    identifier3 = None

    hex_only = re.compile('^[0-9a-fA-F]+$')
    waf_rules = re.compile('^[0-9]+[A-Z]*$')

    cf = CloudFlare.CloudFlare(debug=verbose, raw=raw)

    m = cf
    for element in parts:
        if element[0] == ':':
            element = element[1:]
            if identifier1 is None:
                if len(element) in [32, 40, 48] and hex_only.match(element):
                    # raw identifier - lets just use it as-is
                    identifier1 = element
                elif cmd[0] == 'certificates':
                    # identifier1 = convert_certificates_to_identifier(cf, element)
                    identifier1 = converters.convert_zones_to_identifier(cf, element)
                elif cmd[0] == 'zones':
                    identifier1 = converters.convert_zones_to_identifier(cf, element)
                elif cmd[0] == 'organizations':
                    identifier1 = converters.convert_organizations_to_identifier(cf, element)
                elif (cmd[0] == 'user') and (cmd[1] == 'organizations'):
                    identifier1 = converters.convert_organizations_to_identifier(cf, element)
                elif (cmd[0] == 'user') and (cmd[1] == 'invites'):
                    identifier1 = converters.convert_invites_to_identifier(cf, element)
                elif (cmd[0] == 'user') and (cmd[1] == 'virtual_dns'):
                    identifier1 = converters.convert_virtual_dns_to_identifier(cf, element)
                elif (cmd[0] == 'user') and (cmd[1] == 'load_balancers') and (cmd[2] == 'pools'):
                    identifier1 = converters.convert_load_balancers_pool_to_identifier(cf, element)
                else:
                    exit("/%s/%s :NOT CODED YET 1" % ('/'.join(cmd), element))
                cmd.append(':' + identifier1)
            elif identifier2 is None:
                if len(element) in [32, 40, 48] and hex_only.match(element):
                    # raw identifier - lets just use it as-is
                    identifier2 = element
                elif (cmd[0] and cmd[0] == 'zones') and (cmd[2] and cmd[2] == 'dns_records'):
                    identifier2 = converters.convert_dns_record_to_identifier(cf,
                                                                              identifier1,
                                                                              element)
                else:
                    exit("/%s/%s :NOT CODED YET 2" % ('/'.join(cmd), element))
                # identifier2 may be an array - this needs to be dealt with later
                if isinstance(identifier2, list):
                    cmd.append(':' + '[' + ','.join(identifier2) + ']')
                else:
                    cmd.append(':' + identifier2)
                    identifier2 = [identifier2]
            else:
                if len(element) in [32, 40, 48] and hex_only.match(element):
                    # raw identifier - lets just use it as-is
                    identifier3 = element
                elif waf_rules.match(element):
                    identifier3 = element
                else:
                    exit("/%s/%s :NOT CODED YET 3" % ('/'.join(cmd), element))
        else:
            try:
                m = getattr(m, element)
                cmd.append(element)
            except AttributeError:
                # the verb/element was not found
                if len(cmd) == 0:
                    exit('cli4: /%s - not found' % (element))
                else:
                    exit('cli4: /%s/%s - not found' % ('/'.join(cmd), element))

    results = []
    if identifier2 is None:
        identifier2 = [None]
    for i2 in identifier2:
        try:
            if method is 'GET':
                r = m.get(identifier1=identifier1,
                          identifier2=i2,
                          identifier3=identifier3,
                          params=params)
            elif method is 'PATCH':
                r = m.patch(identifier1=identifier1,
                            identifier2=i2,
                            identifier3=identifier3,
                            data=params)
            elif method is 'POST':
                r = m.post(identifier1=identifier1,
                           identifier2=i2,
                           identifier3=identifier3,
                           data=params)
            elif method is 'PUT':
                r = m.put(identifier1=identifier1,
                          identifier2=i2,
                          identifier3=identifier3,
                          data=params)
            elif method is 'DELETE':
                r = m.delete(identifier1=identifier1,
                             identifier2=i2,
                             identifier3=identifier3,
                             data=params)
            else:
                pass
        except CloudFlare.exceptions.CloudFlareAPIError as e:
            if len(e) > 0:
                # more than one error returned by the API
                for x in e:
                    sys.stderr.write('cli4: /%s - %d %s\n' % (command, x, x))
            exit('cli4: /%s - %d %s' % (command, e, e))
        except Exception as e:
            exit('cli4: /%s - %s - api error' % (command, e))

        results.append(r)

    if len(results) == 1:
        results = results[0]

    if output == 'json':
        sys.stdout.write(json.dumps(results, indent=4, sort_keys=True) + '\n')
    if output == 'yaml':
        sys.stdout.write(yaml.safe_dump(results))

