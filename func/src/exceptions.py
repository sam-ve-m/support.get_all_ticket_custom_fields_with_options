class ErrorToGetRedisClient(Exception):
    def __init__(self):
        self.msg = 'Error on get Redis client connection.'
        self.status_code = 500


class ErrorToRequestZendeskApi(Exception):
    def __init__(self):
        self.msg = 'Failed to request ticket custom fields to Zendesk Api.'
        self.status_code = 400


class InvalidEndpointZendeskApi(Exception):
    def __init__(self):
        self.msg = 'Invalid Endpoint for Zendesk Api.'
        self.status_code = 404
