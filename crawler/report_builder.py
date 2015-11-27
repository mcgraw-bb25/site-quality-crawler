import os
import json
import datetime

from crawler.page_report import PageReport


class ReportBuilder(PageReport):
    ''' Builds a JSON from a list of PageReports '''
    def __init__(self, page_reports):
        self.page_reports = page_reports
        self.json_report = ""

    def build_report(self):
        ''' Method builds the report '''
        self.replace_urls_with_ids()
        pr_dictionary = [pr.get_dictionary() for pr in self.page_reports]
        self.json_report = json.dumps(pr_dictionary, indent=4)
        self.save_report()

    def replace_urls_with_ids(self):
        '''
        Replaces URLs in page reports page_links with
        their respective PageReport ID
        '''
        # Build page report dictionary {url : id}
        pr_set = {}
        for pr in self.page_reports:
            pr_set[pr.url] = pr.id

        # Replace URLs in page_links with PageReport ID
        for pr in self.page_reports:
            for i in range(len(pr.page_links)):
                try:
                    page_id = pr_set[pr.page_links[i]]
                    pr.page_links[i] = page_id
                except KeyError:
                    pr.page_links[i] = None
            # The visualization will throw an error on unknown IDs
            # We remove the key errors below
            pr.page_links = list(filter(None, pr.page_links))

    def save_report(self):
        ''' Method to implement saving report '''
        now = datetime.datetime.now()
        timestamp_string = str(now.year) \
            + "_" + str(now.month) \
            + "_" + str(now.day) \
            + "_" + str(now.hour) \
            + "_" + str(now.minute) \
            + "_" + str(now.second)

        curpath = os.getcwd()
        file_path = curpath + '/reports/'
        file_name = file_path + 'site_report-' + timestamp_string + '.json'

        print("Saving report to %s" % file_name)
        with open(file_name, 'w') as reportfile:
            reportfile.write(self.json_report)
