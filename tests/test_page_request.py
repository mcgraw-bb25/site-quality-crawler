import unittest
from tests.mock_classes import MockRequestWrapper
from crawler.page_request import PageRequest


class MockPageRequest(PageRequest, MockRequestWrapper):
    pass


class PageRequestUnitTest(unittest.TestCase):
    def test_001(self):
        ''' Looks at a real url and confirms text isn't blank '''
        real_site = 'http://www.duckduckgo.com'
        real_request_test = PageRequest(real_site).make_request()
        self.assertIsNotNone(real_request_test.text)

    def test_002(self):
        ''' Looks at a mock url '''
        mock_site = 'localtestsite.com'
        mock_request_test = MockPageRequest(mock_site).make_request()
        self.assertEqual(mock_request_test.text, "<html>")
        self.assertEqual(mock_request_test.content, b"<html>")

if __name__ == "__main__":
    unittest.main()
