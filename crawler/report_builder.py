import os
import json
import datetime

from crawler.page_report import PageReport


class ReportBuilder(PageReport):
    '''
    This takes in a set of PageReports
    and builds a clean json report
    '''

    def __init__(self, pages):
        self.pages = pages

        # build_report method returns a string
        self.report = ""

    def clean_pageid(self):
        '''
        This method cleans the page ids in page report
        so that page_links receives the hashes rather than the url

        Invoked by start_crawl()
        Probably requires a discussion with Mateusz sometime
        '''

        # initialize dictionary to hold url : id
        page_set = {}

        # run through page reports and append to page_set dic
        for page in self.pages:
            url_name = page.url
            url_id = page.id
            page_set[url_name] = url_id

        # run through page reports again and swap page_links url with id
        for page in self.pages:
            position_counter = 0
            for i in range(len(page.page_links)):
                try:
                    page_id = page_set[page.page_links[i]]
                    page.page_links[i] = page_id
                except:
                    continue
            position_counter = position_counter + 1

    def build_report(self):
        ''' Method builds the report '''
        # calls clean_pageid to prepare data to build report into
        self.clean_pageid()

        # calls Mateusz's function to publish json item for each page
        self.report = json.dumps([page.get_dictionary() for page in self.pages])

        self.save_report()

    def save_report(self):
        ''' Method to implement saving report '''

        timestamp = str(datetime.datetime.now().year) \
            + "_" + str(datetime.datetime.now().month) \
            + "_" + str(datetime.datetime.now().day) \
            + "_" + str(datetime.datetime.now().minute) \
            + "_" + str(datetime.datetime.now().second)

        curpath = os.getcwd()
        newpath = curpath + '/reports/'
        newfile = newpath + 'site_report' + timestamp + '.json'

        with open(newfile, 'w') as reportfile:
            reportfile.write(self.report)
