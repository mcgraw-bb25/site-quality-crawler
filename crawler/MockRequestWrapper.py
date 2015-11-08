from RequestWrapper import RequestWrapper
import unittest


class MockResponseObject(object):
    '''
    This class creates a mock response object to return when
    called by MockRequestWrapper.
    Requests makes use of request and returns a response object,
    this MockResponseObject is the counter to the MockRequestWrapper.

    Two methods, __init__ and make_response
    '''

    def __init__(self):
        self.text = "<html>"
        self.content = self.text.encode()

    def make_response(self):
        '''
        This method returns self to caller.
        Caller should be MockRequestWrapper
        '''

        return self


class MockRequestWrapper(RequestWrapper):
    '''
    This is object which mocks requests.request

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

        mock_response_object = MockResponseObject()
        response = mock_response_object.make_response()
        return response


class RequestWrapperUnitTest(unittest.TestCase):

    def test_001(self):
        '''
        Sets up and executes test on MockRequestWrapper and MockResponseObject
        which are tested in this file only.
        These are really a library that allow PageRequest.py
        to run integration tests.
        '''
        # Test setup and initialization
        mock_site = "localsite.com"
        mock_request = MockRequestWrapper(mock_site)
        mock_response = mock_request.make_request()

        # Tests
        self.assertEqual(mock_response.text, "<html>")
        self.assertNotEqual(mock_response.text, "</html>")
        self.assertEqual(mock_response.content, b"<html>")
        self.assertNotEqual(mock_response.content, b"</html>")


if __name__ == "__main__":

    unittest.main()
