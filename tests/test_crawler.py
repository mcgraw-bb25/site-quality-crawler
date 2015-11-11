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

    def test_002(self):
        ''' Tests output of mock crawler '''

        # initialize test report file output
        curpath = os.getcwd()
        newpath = curpath + '/reports/'
        newfile = newpath + 'mock_site_report.json'

        with open(newfile, 'r') as mockjsonreport:
            mock_json_report = mockjsonreport.read()

        # print (mock_json_report)
        self.assertIsNotNone(mock_json_report)
        self.assertIn('www.localtestsite.com/mysite.html', mock_json_report)
        self.assertIn('www.localtestsite.com/aboutus.html', mock_json_report)
        self.assertIn('www.localtestsite.com/login.html', mock_json_report)

        '''
        This entire section doesn't work because the dict builder
        produces different json files on each run.

        Should discuss with Mateusz

        # initialize known test output
        curpath = os.getcwd()
        newpath = curpath + '/tests/'
        newfile = newpath + 'mock_test_output.json'

        with open(newfile, 'r') as knownjsonreport:
            known_json_report = knownjsonreport.read()

        print (known_json_report)
        self.assertIsNotNone(known_json_report)

        self.assertEqual(mock_json_report, known_json_report)
        '''
