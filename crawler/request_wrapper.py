import requests


class RequestTypeError(Exception):
    ''' Initialize Error Object for RequestWrapper '''
    pass


class RequestWrapper(object):
    '''
    Wrapper for the requests library
    Exposes two methods: get and post
    '''
    def __init__(self, url, req_type="GET"):
        self.url = url
        self.req_type = req_type.upper()

    def make_request(self):
        '''
        Executes calls to the requests API
        '''
        if self.req_type == "GET":
            response = requests.get(self.url)
        elif self.req_type == "POST":
            response = requests.post(self.url)
        else:
            raise RequestTypeError("ERROR - Invalid request type")

        return response
