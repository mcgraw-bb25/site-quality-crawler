import unittest

from RequestWrapper import RequestWrapper
from MockRequestWrapper import MockRequestWrapper


class PageRequest(RequestWrapper):
    '''
    This class initializes with a url and has only a single method - crawl
    Crawl calls super() to make_request().
    Since PageRequest inherits from RequestWrapper, PageRequest will
    make a call to RequestWrapper.make_request() under normal circumstances.

    However MockPageRequest inherits from MockRequestWrapper as well
    and super() allows to inject the mocking dependencies which allow
    for integration testing of the entire application.
    '''
    def __init__(self, url):
        ''' May want to clean up use of super into init '''
        self.url = url

    def crawl(self):
        '''
        Calls super() to initialize either RequestWrapper/MockRequestWrapper
        Creates a variable called response, which needs to know that
        request method make_request, and contains the logic of the crawler
        Returns the entire response object
        '''
        super().__init__(self.url)
        # print ("Hitting %s url" % (self.url))
        response = super().make_request()
        # print (response.text[0:50])

        return response


class MockPageRequest(PageRequest, MockRequestWrapper):
    pass


class PageRequestUnitTest(unittest.TestCase):
    ''' Class contains two unit tests for PageRequest '''

    def test_001(self):
        ''' Test 1 looks at a real url and confirms text isn't blank '''
        real_site = 'http://www.duckduckgo.com'
        real_request_test = PageRequest(real_site).crawl()
        self.assertIsNotNone(real_request_test.text)

    def test_002(self):
        ''' Test 2 looks at a mock url '''
        mock_site = 'notarealsite.com'
        mock_request_test = MockPageRequest(mock_site).crawl()
        self.assertEqual(mock_request_test.text, "<html>")
        self.assertEqual(mock_request_test.content, b"<html>")


if __name__ == "__main__":

    unittest.main()
