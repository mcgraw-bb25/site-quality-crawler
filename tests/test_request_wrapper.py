import unittest
from crawler.request_wrapper import RequestWrapper, RequestTypeError
from tests.mock_classes import MockRequestWrapper


class RequestWrapperUnitTest(unittest.TestCase):
    def test_001(self):
        ''' Looks at a real url and confirms text isn't blank '''
        real_site = 'https://duckduckgo.com'
        real_request = RequestWrapper(real_site).make_request()
        self.assertIsNotNone(real_request.text)

    def test_002(self):
        ''' Looks at a real url with a bad request type '''
        real_site = 'https://duckduckgo.com'
        request = RequestWrapper(real_site, "ZZZ")
        self.assertRaises(RequestTypeError, request.make_request)

    def test_003(self):
        ''' Hits a real url with a lowercase request type '''
        real_site = 'https://duckduckgo.com'
        real_request = RequestWrapper(real_site, "get").make_request()
        self.assertIsNotNone(real_request.text)

    def test_004(self):
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
