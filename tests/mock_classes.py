from crawler.request_wrapper import RequestWrapper

import os


class MockResponse(object):
    ''' A mock response object returned by MockRequestWrapper '''
    def __init__(self):
        ''' Initializes to a false state to force test coverage '''
        self.text = "false data"
        self.content = self.text.encode()

    def set_text(self, text):
        ''' Simple setter method for mocking '''
        self.text = text
        self.content = text.encode()

    def fetch_response(self, filename):
        ''' Handles the file opening methods and returns text '''

        with open(filename, 'r') as testhtml:
            test_response_data = testhtml.read()

        return test_response_data

    def make_response(self, url):
        '''
        Takes in url and sets the responses appropriately
        Returns self to object caller
        '''

        curpath = os.getcwd()
        newpath = curpath + '/tests/example-sites/'

        if url == "localtestsite.com":
            test_response_data = "<html>"
            self.set_text(test_response_data)
        elif url == "http://www.localtestsite.com/mysite.html":
            testfile = newpath + 'mysite.html'
            test_response_data = self.fetch_response(testfile)
            self.set_text(test_response_data)
        elif url == "http://www.localtestsite.com/aboutus.html":
            testfile = newpath + 'aboutus.html'
            test_response_data = self.fetch_response(testfile)
            self.set_text(test_response_data)
        elif url == "http://www.localtestsite.com/login.html":
            testfile = newpath + 'login.html'
            test_response_data = self.fetch_response(testfile)
            self.set_text(test_response_data)

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
        response = mock_response_object.make_response(self.url)
        return response
