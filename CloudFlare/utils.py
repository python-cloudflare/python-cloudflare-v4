""" misc utilities  for Cloudflare API"""
from __future__ import absolute_import

import sys
import requests

from . import __version__

def user_agent():
    """ misc utilities  for Cloudflare API"""
    # the default User-Agent is something like 'python-requests/2.11.1'
    # this additional data helps support @ Cloudflare help customers
    return ('python-cloudflare/' + __version__ + '/' +
            'python-requests/' + str(requests.__version__) + '/' +
            'python/' + '.'.join(map(str, sys.version_info[:3]))
           )

def sanitize_secrets(secrets):
    """ misc utilities  for Cloudflare API"""
    redacted_phrase = 'REDACTED'

    if secrets is None:
        return None

    secrets_copy = secrets.copy()
    if 'password' in secrets_copy:
        secrets_copy['password'] = redacted_phrase
    elif 'X-Auth-Key' in secrets_copy:
        secrets_copy['X-Auth-Key'] = redacted_phrase
    elif 'X-Auth-User-Service-Key' in secrets_copy:
        secrets_copy['X-Auth-User-Service-Key'] = redacted_phrase

    return secrets_copy
