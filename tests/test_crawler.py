import unittest
import json
import os

# from crawler.crawler import Crawler
from tests.mock_classes import MockCrawler
from pprint import pprint


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

        self.assertIn('/mysite.html', mock_json_data)
        self.assertIn('/aboutus.html', mock_json_data)
        self.assertIn('/login.html', mock_json_data)

        curpath = os.getcwd()
        newpath = curpath + '/reports/'
        newfile = newpath + 'mock_site_report.json'

        with open(newfile, 'w') as mockjson:
            mockjson.write(mock_json_data)

    def test_002(self):
        ''' Tests output of mock crawler '''

        # initialize test report file output
        curpath = os.getcwd()
        newpath = curpath + '/reports/'
        newfile = newpath + 'mock_site_report.json'

        with open(newfile, 'r') as mockjsonreport:
            mock_json_report = mockjsonreport.read()
        
        mock_json_report = json.loads(mock_json_report)
        
        sorted_mock_json_report = sorted(mock_json_report,
                                        key=lambda item: item['id'])
        
        self.assertIsNotNone(mock_json_report)
        self.assertEqual(len(sorted_mock_json_report), 3)
        self.assertEqual("2ab6b60a90d8cb488975931523f2c401",\
                                    sorted_mock_json_report[0]['id'])
        self.assertEqual("c1260fd9d3d8e6ab5ddf493668b98537",\
                                    sorted_mock_json_report[1]['id'])
        self.assertEqual("fc063341aba1a257f83bb1652eac3079",\
                                    sorted_mock_json_report[2]['id'])
        self.assertIn("fc063341aba1a257f83bb1652eac3079",\
                                    sorted_mock_json_report[0]['page_links'])
        self.assertIn("c1260fd9d3d8e6ab5ddf493668b98537",\
                                    sorted_mock_json_report[0]['page_links'])

if __name__ == "__main__":
    unittest.main()
