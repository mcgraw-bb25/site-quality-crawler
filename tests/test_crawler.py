import unittest
import json

# from crawler.crawler import Crawler
from tests.mock_classes import MockCrawler


class CrawlerUnitTest(unittest.TestCase):
    '''
    Tests the crawler with a MockCrawler object on local html
    MockCrawler only over loads one function to allow mock
    '''

    def test_001(self):
        ''' Tests mock crawler '''
        mock_crawler = MockCrawler(
            root_url='http://www.localtestsite.com/',
            start_url='http://www.localtestsite.com/mysite.html')
        mock_crawler.start_crawl()
        print (json.dumps([pr.get_dictionary() \
                for pr in mock_crawler.page_reports]))
        self.assertEqual('a', 'a')
