import unittest
import json
import os

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

        # returns a string
        mock_json_data = (json.dumps([pr.get_dictionary()
                          for pr in mock_crawler.page_reports]))

        self.assertIn('www.localtestsite.com/mysite.html', mock_json_data)
        self.assertIn('www.localtestsite.com/aboutus.html', mock_json_data)
        self.assertIn('www.localtestsite.com/login.html', mock_json_data)

        curpath = os.getcwd()
        newpath = curpath + '/reports/'
        newfile = newpath + 'mock_site_report.json'

        with open(newfile, 'w') as mockjson:
            mockjson.write(mock_json_data)

        # print (mock_json_data)
