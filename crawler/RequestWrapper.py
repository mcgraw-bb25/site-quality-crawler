import requests
import unittest


class RequestTypeError(Exception):
    ''' Initialize Error Object for RequestWrapper '''
    pass


class RequestWrapper(object):
    '''
    This class wraps the requests library and allows access to
    two methods: get and post.
    Rather than having requests exposed to application it
    has been left in this libray.  This library also introduces
    testing framework which allows mocking data for
    integration testing.  This is implemented in MockRequestWrapper.py
    '''

    def __init__(self, url, req_type="GET"):
        self.url = url
        self.req_type = req_type.upper()

    def make_request(self):
        '''
        This method executes the calls to the requests API.
        Any changes can be concentrated into this method
        in the future.
        '''
        if self.req_type == "GET":
            response = requests.get(self.url)
        elif self.req_type == "POST":
            response = requests.post(self.url)
        else:
            raise RequestTypeError("ERROR - Invalid request type")

        return response


class RequestWrapperUnitTest(unittest.TestCase):
    '''
    Class contains three unit tests for RequestWrapper
    Should look into further developing these in the future.
    '''

    def test_001(self):
        ''' Test 1 looks at a real url and confirms text isn't blank '''
        real_site = 'https://duckduckgo.com'
        real_request = RequestWrapper(real_site).make_request()
        self.assertIsNotNone(real_request.text)

    def test_002(self):
        ''' Test 2 looks at a real url with a bad request type '''
        real_site = 'https://duckduckgo.com'
        request = RequestWrapper(real_site, "ZZZ")
        self.assertRaises(RequestTypeError, request.make_request)

    def test_003(self):
        ''' Test 3 hits a real url with a lowercase request type '''
        real_site = 'https://duckduckgo.com'
        real_request = RequestWrapper(real_site, "get").make_request()
        self.assertIsNotNone(real_request.text)


if __name__ == "__main__":

    unittest.main()
