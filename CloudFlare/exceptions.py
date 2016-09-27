""" errors for CloudFlare API"""

class CloudFlareError(Exception):
    """ errors for CloudFlare API"""

    def __init__(self, code, message):
        """ errors for CloudFlare API"""

        self.code = code
        self.message = message

    def __int__(self):
        """ errors for CloudFlare API"""

        return self.code

    def __str__(self):
        """ errors for CloudFlare API"""

        return self.message

class CloudFlareAPIError(CloudFlareError):
    """ errors for CloudFlare API"""

    pass

class CloudFlareInternalError(CloudFlareError):
    """ errors for CloudFlare API"""

    pass

