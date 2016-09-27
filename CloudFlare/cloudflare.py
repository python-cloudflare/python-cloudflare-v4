""" CloudFlare v4 API"""

import json
import urllib
import requests

from logger import Logger
from utils import sanitize_secrets
from read_configs import read_configs
from api_v4 import api_v4
from api_extras import api_extras
from exceptions import CloudFlareError, CloudFlareAPIError, CloudFlareInternalError

BASE_URL = 'https://api.cloudflare.com/client/v4'

class CloudFlare(object):
    """ CloudFlare v4 API"""

    class _base(object):
        """ CloudFlare v4 API"""

        def __init__(self, email, token, certtoken, base_url, debug):
            """ CloudFlare v4 API"""

            self.email = email
            self.token = token
            self.certtoken = certtoken
            self.base_url = base_url

            if debug:
                self.logger = Logger(debug).getLogger()
            else:
                self.logger = None

        def call_with_no_auth(self, method,
                              api_call_part1,
                              api_call_part2=None,
                              api_call_part3=None,
                              identifier1=None, identifier2=None,
                              params=None, data=None):
            """ CloudFlare v4 API"""

            headers = {
                'Content-Type': 'application/json'
            }
            return self._call(method, headers,
                              api_call_part1, api_call_part2, api_call_part3,
                              identifier1, identifier2,
                              params, data)

        def call_with_auth(self, method,
                           api_call_part1,
                           api_call_part2=None,
                           api_call_part3=None,
                           identifier1=None, identifier2=None,
                           params=None, data=None):
            """ CloudFlare v4 API"""

            if self.email is '' or self.token is '':
                raise CloudFlareAPIError(0, 'no email and/or token defined')
            headers = {
                'X-Auth-Email': self.email,
                'X-Auth-Key': self.token,
                'Content-Type': 'application/json'
            }
            return self._call(method, headers,
                              api_call_part1, api_call_part2, api_call_part3,
                              identifier1, identifier2,
                              params, data)

        def call_with_certauth(self, method,
                               api_call_part1,
                               api_call_part2=None,
                               api_call_part3=None,
                               identifier1=None, identifier2=None,
                               params=None, data=None):
            """ CloudFlare v4 API"""

            if self.certtoken is '':
                raise CloudFlareAPIError(0, 'no email and/or cert token defined')
            headers = {
                'X-Auth-User-Service-Key': self.certtoken,
                'Content-Type': 'application/json'
            }
            return self._call(method, headers,
                              api_call_part1, api_call_part2, api_call_part3,
                              identifier1, identifier2,
                              params, data)

        def _call(self, method, headers,
                  api_call_part1,
                  api_call_part2=None,
                  api_call_part3=None,
                  identifier1=None, identifier2=None,
                  params=None, data=None):
            """ CloudFlare v4 API"""

            if api_call_part2 is not None or (data is not None and method == 'GET'):
                if identifier2 is None:
                    url = (self.base_url + '/'
                           + api_call_part1 + '/'
                           + identifier1 + '/'
                           + api_call_part2)
                else:
                    url = (self.base_url + '/'
                           + api_call_part1 + '/'
                           + identifier1 + '/'
                           + api_call_part2 + '/'
                           + identifier2)
            else:
                if identifier1 is None:
                    url = (self.base_url + '/'
                           + api_call_part1)
                else:
                    url = (self.base_url + '/'
                           + api_call_part1 + '/'
                           + identifier1)
            if api_call_part3:
                url += '/' + api_call_part3

            if self.logger:
                self.logger.debug('Call: %s,%s,%s,%s,%s' % (str(api_call_part1),
                                                            str(identifier1),
                                                            str(api_call_part2),
                                                            str(identifier2),
                                                            str(api_call_part3)))
                self.logger.debug('Call: optional params and data %s %s' % (str(params),
                                                                            str(data)))
                self.logger.debug('Call: method and url %s %s' % (str(method), str(url)))
                self.logger.debug('Call: headers %s' % str(sanitize_secrets(headers)))

            if (method is None) or (api_call_part1 is None):
                # should never happen
                raise CloudFlareInternalError(0, 'You must specify a method and endpoint')

            method = method.upper()

            if self.logger:
                self.logger.debug('Call: doit!')

            try:
                if method == 'GET':
                    response = requests.get(url, headers=headers, params=params, data=data)
                elif method == 'POST':
                    response = requests.post(url, headers=headers, params=params, json=data)
                elif method == 'PUT':
                    response = requests.put(url, headers=headers, params=params, json=data)
                elif method == 'DELETE':
                    response = requests.delete(url, headers=headers, json=data)
                elif method == 'PATCH':
                    response = requests.request('PATCH', url,
                                                headers=headers, params=params, json=data)
                else:
                    # should never happen
                    raise CloudFlareAPIError(0, 'method not supported')
                if self.logger:
                    self.logger.debug('Call: done!')
            except Exception as e:
                if self.logger:
                    self.logger.debug('Call: exception!')
                raise CloudFlareAPIError(0, 'connection failed.')

            if self.logger:
                self.logger.debug('Response: url %s', response.url)

            response_data = response.text
            if self.logger:
                self.logger.debug('Response: data %s' % response_data)
            try:
                response_data = json.loads(response_data)
            except ValueError:
                raise CloudFlareAPIError(0, 'JSON parse failed.')

            if response_data['success'] is False:
                code = response_data['errors'][0]['code']
                message = response_data['errors'][0]['message']
                if len(response_data['messages'])>0:
                        detailmessage = ' Detailed message: '+response_data['messages'][0]['message']
                else:
                        detailmessage = ''
                if self.logger:
                    self.logger.debug('Response: error %d %s %s' % (code, message, detailmessage))
                raise CloudFlareAPIError(code, message+detailmessage)

            result = response_data['result']
            if self.logger:
                self.logger.debug('Response: %s' % (result))
            return result

    class add_unused(object):
        """ CloudFlare v4 API"""

        def __init__(self, base, api_call_part1, api_call_part2=None, api_call_part3=None):
            """ CloudFlare v4 API"""

            self.base = base
            self.api_call_part1 = api_call_part1
            self.api_call_part2 = api_call_part2
            self.api_call_part3 = api_call_part3

    class add_noauth(object):
        """ CloudFlare v4 API"""

        def __init__(self, base, api_call_part1, api_call_part2=None, api_call_part3=None):
            """ CloudFlare v4 API"""

            self.base = base
            self.api_call_part1 = api_call_part1
            self.api_call_part2 = api_call_part2
            self.api_call_part3 = api_call_part3

        def get(self, identifier1=None, identifier2=None, params=None, data=None):
            """ CloudFlare v4 API"""

            return self.base.call_with_no_auth('GET',
                                               self.api_call_part1,
                                               self.api_call_part2,
                                               self.api_call_part3,
                                               identifier1, identifier2,
                                               params, data)

    class add_with_auth(object):
        """ CloudFlare v4 API"""

        def __init__(self, base, api_call_part1, api_call_part2=None, api_call_part3=None):
            """ CloudFlare v4 API"""

            self.base = base
            self.api_call_part1 = api_call_part1
            self.api_call_part2 = api_call_part2
            self.api_call_part3 = api_call_part3

        def get(self, identifier1=None, identifier2=None, params=None, data=None):
            """ CloudFlare v4 API"""

            return self.base.call_with_auth('GET',
                                            self.api_call_part1,
                                            self.api_call_part2,
                                            self.api_call_part3,
                                            identifier1, identifier2,
                                            params, data)

        def patch(self, identifier1=None, identifier2=None, params=None, data=None):
            """ CloudFlare v4 API"""

            return self.base.call_with_auth('PATCH',
                                            self.api_call_part1,
                                            self.api_call_part2,
                                            self.api_call_part3,
                                            identifier1, identifier2,
                                            params, data)

        def post(self, identifier1=None, identifier2=None, params=None, data=None):
            """ CloudFlare v4 API"""

            return self.base.call_with_auth('POST',
                                            self.api_call_part1,
                                            self.api_call_part2,
                                            self.api_call_part3,
                                            identifier1, identifier2,
                                            params, data)

        def put(self, identifier1=None, identifier2=None, params=None, data=None):
            """ CloudFlare v4 API"""

            return self.base.call_with_auth('PUT',
                                            self.api_call_part1,
                                            self.api_call_part2,
                                            self.api_call_part3,
                                            identifier1, identifier2,
                                            params, data)

        def delete(self, identifier1=None, identifier2=None, params=None, data=None):
            """ CloudFlare v4 API"""

            return self.base.call_with_auth('DELETE',
                                            self.api_call_part1,
                                            self.api_call_part2,
                                            self.api_call_part3,
                                            identifier1, identifier2,
                                            params, data)

    class add_with_cert_auth(object):
        """ CloudFlare v4 API"""

        def __init__(self, base, api_call_part1, api_call_part2=None, api_call_part3=None):
            """ CloudFlare v4 API"""

            self.base = base
            self.api_call_part1 = api_call_part1
            self.api_call_part2 = api_call_part2
            self.api_call_part3 = api_call_part3

        def get(self, identifier1=None, identifier2=None, params=None, data=None):
            """ CloudFlare v4 API"""

            return self.base.call_with_certauth('GET',
                                                self.api_call_part1,
                                                self.api_call_part2,
                                                self.api_call_part3,
                                                identifier1, identifier2,
                                                params, data)

        def patch(self, identifier1=None, identifier2=None, params=None, data=None):
            """ CloudFlare v4 API"""

            return self.base.call_with_certauth('PATCH',
                                                self.api_call_part1,
                                                self.api_call_part2,
                                                self.api_call_part3,
                                                identifier1, identifier2,
                                                params, data)

        def post(self, identifier1=None, identifier2=None, params=None, data=None):
            """ CloudFlare v4 API"""

            return self.base.call_with_certauth('POST',
                                                self.api_call_part1,
                                                self.api_call_part2,
                                                self.api_call_part3,
                                                identifier1, identifier2,
                                                params, data)

        def put(self, identifier1=None, identifier2=None, params=None, data=None):
            """ CloudFlare v4 API"""

            return self.base.call_with_certauth('PUT',
                                                self.api_call_part1,
                                                self.api_call_part2,
                                                self.api_call_part3,
                                                identifier1, identifier2,
                                                params, data)

        def delete(self, identifier1=None, identifier2=None, params=None, data=None):
            """ CloudFlare v4 API"""

            return self.base.call_with_certauth('DELETE',
                                                self.api_call_part1,
                                                self.api_call_part2,
                                                self.api_call_part3,
                                                identifier1, identifier2,
                                                params, data)

    def __init__(self, email=None, token=None, certtoken=None, debug=False):
        """ CloudFlare v4 API"""

        base_url = BASE_URL

        # class creation values override configuration values
        [conf_email, conf_token, conf_certtoken, extras] = read_configs()

        if email is None:
            email = conf_email
        if token is None:
            token = conf_token
        if certtoken is None:
            certtoken = conf_certtoken

        self.base = self._base(email, token, certtoken, base_url, debug)

        # add the API calls
        api_v4(self)
        if extras:
            api_extras(self, extras)
