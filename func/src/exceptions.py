class ErrorToRequestZendeskApi(Exception):
    def __init__(self):
        self.msg = 'Failed to request ticket custom fields to Zendesk Api.'


class InvalidEndpointZendeskApi(Exception):
    def __init__(self):
        self.msg = 'Invalid Endpoint for Zendesk Api.'