"""Cloudflare API via command line"""
from __future__ import absolute_import

import CloudFlare

def convert_zones_to_identifier(cf, zone_name):
    """zone names to numbers"""
    params = {'name':zone_name, 'per_page':1}
    try:
        zones = cf.zones.get(params=params)
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('cli4: %s - %d %s' % (zone_name, e, e))
    except Exception as e:
        exit('cli4: %s - %s' % (zone_name, e))

    if len(zones) == 1:
        return zones[0]['id']

    exit('cli4: %s - zone not found' % (zone_name))

def convert_dns_record_to_identifier(cf, zone_id, dns_name):
    """dns record names to numbers"""
    # this can return an array of results as there can be more than one DNS entry for a name.
    params = {'name':dns_name}
    try:
        dns_records = cf.zones.dns_records.get(zone_id, params=params)
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('cli4: %s - %d %s' % (dns_name, e, e))
    except Exception as e:
        exit('cli4: %s - %s' % (dns_name, e))

    r = []
    for dns_record in dns_records:
        if dns_name == dns_record['name']:
            r.append(dns_record['id'])
    if len(r) > 0:
        return r

    exit('cli4: %s - dns name not found' % (dns_name))

def convert_certificates_to_identifier(cf, certificate_name):
    """certificate names to numbers"""
    try:
        certificates = cf.certificates.get()
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('cli4: %s - %d %s' % (certificate_name, e, e))
    except Exception as e:
        exit('cli4: %s - %s' % (certificate_name, e))

    for certificate in certificates:
        if certificate_name in certificate['hostnames']:
            return certificate['id']

    exit('cli4: %s - no zone certificates found' % (certificate_name))

def convert_organizations_to_identifier(cf, organization_name):
    """organizations names to numbers"""
    try:
        organizations = cf.user.organizations.get()
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('cli4: %s - %d %s' % (organization_name, e, e))
    except Exception as e:
        exit('cli4: %s - %s' % (organization_name, e))

    for organization in organizations:
        if organization_name == organization['name']:
            return organization['id']

    exit('cli4: %s - no organizations found' % (organization_name))

def convert_invites_to_identifier(cf, invite_name):
    """invite names to numbers"""
    try:
        invites = cf.user.invites.get()
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('cli4: %s - %d %s' % (invite_name, e, e))
    except Exception as e:
        exit('cli4: %s - %s' % (invite_name, e))

    for invite in invites:
        if invite_name == invite['organization_name']:
            return invite['id']

    exit('cli4: %s - no invites found' % (invite_name))

def convert_virtual_dns_to_identifier(cf, virtual_dns_name):
    """virtual dns names to numbers"""
    try:
        virtual_dnss = cf.user.virtual_dns.get()
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('cli4: %s - %d %s\n' % (virtual_dns_name, e, e))
    except Exception as e:
        exit('cli4: %s - %s\n' % (virtual_dns_name, e))

    for virtual_dns in virtual_dnss:
        if virtual_dns_name == virtual_dns['name']:
            return virtual_dns['id']

    exit('cli4: %s - no virtual_dns found' % (virtual_dns_name))

def convert_load_balancers_pool_to_identifier(cf, pool_name):
    """load balancer pool names to numbers"""
    try:
        pools = cf.user.load_balancers.pools.get()
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('cli4: %s - %d %s' % (pool_name, e, e))
    except Exception as e:
        exit('cli4: %s - %s' % (pool_name, e))

    for p in pools:
        if pool_name == p['description']:
            return p['id']

    exit('cli4: %s - no pools found' % (pool_name))

