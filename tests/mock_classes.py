from crawler.request_wrapper import RequestWrapper


class MockResponse(object):
    ''' A mock response object returned by MockRequestWrapper '''
    def __init__(self):
        self.text = "<html>"
        self.content = self.text.encode()

    def make_response(self):
        ''' Returns self to object caller '''
        return self


class MockRequestWrapper(RequestWrapper):
    '''
    Mock for requests.request

    Three methods, __init__, make_request, get_response
    make_request is the public method that RequestWrapper shares
    and through the use of super in PageRequest we can mock
    that object out.

    get_response is a method which specifically speaks to
    MockResponseObject and leaves implementation of that object
    able to change in the future.
    '''
    def __init__(self, url, req_type="GET"):
        self.url = url
        self.req_type = req_type.upper()

    def make_request(self):
        '''
        This method mocks a request from Requests library.
        It inherits from both RequestWrapper and MockResponseObject.
        Should call MockResponseObject and pass back mock response.
        '''
        return self.get_response()

    def get_response(self):
        '''
        This method carries the dependency to MockResponseObject
        Passes back response
        '''
        mock_response_object = MockResponse()
        response = mock_response_object.make_response()
        return response
