import time
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from crawler.page_request import PageRequest
from crawler.page_report import PageReport
from crawler.report_builder import ReportBuilder


class Crawler(object):
    '''
    The main crawler object that the user interacts with
    '''
    crawled_urls = []
    page_reports = []

    def __init__(self, root_url, start_url=None, crawl_limit=5):
        self.root_url = root_url
        if start_url:
            self.start_url = start_url
        else:
            self.start_url = root_url
        self.crawl_limit = crawl_limit

    def start_crawl(self):
        '''
        Begins crawling the given site at the initialized start_url
        '''
        self.url_queue = [self.start_url]
        while self.url_queue and len(self.crawled_urls) < self.crawl_limit:
            current_url = self.url_queue.pop(0)

            if current_url in self.crawled_urls:
                continue
            if self.is_outbound_url(current_url):
                print("Skipping outbound url ", current_url)
                continue

            try:
                response = self.get_response(current_url)
            except:
                # TODO: Put malformed urls in page report
                print('Skipping malformed URL - ', current_url)
                continue

            page_report = PageReport(
                url=current_url,
                status_code=response.status_code,
                redirects=response.history,
                page_links=self.get_absolute_page_links(current_url, response))

            self.url_queue += page_report.page_links
            self.page_reports.append(page_report)
            self.crawled_urls.append(current_url)
            self.sleep()

        self.build_report()

    def get_response(self, current_url):
        ''' Hides PageRequest which allows for mocking '''
        return PageRequest(current_url).make_request()

    def get_absolute_page_links(self, current_url, response):
        '''
        Parses a page and returns all links on the page in absolute form
        '''
        page_soup = BeautifulSoup(response.content, 'html.parser')
        links = []
        for tag in page_soup.find_all('a'):
            if tag.has_attr('href'):
                url = self.get_absolute_url(current_url, tag.get('href'))
                if not self.is_outbound_url(url):
                    links.append(url)
        return links

    def get_absolute_url(self, base_url, link_url):
        '''
        Given a root and a url returns the absolute url
        '''
        if link_url.startswith('http://') or link_url.startswith('https://'):
            return link_url
        return urljoin(base_url, link_url)

    def is_outbound_url(self, url):
        '''
        Returns true when url is outside the domain of the root url
        '''
        return not url.startswith(self.root_url)

    def sleep(self):
        '''
        Used to delay between requests while crawling
        '''
        time.sleep(2)

    def build_report(self):
        ''' invokes ReportBuilder '''
        ReportBuilder(self.page_reports).build_report()


if __name__ == '__main__':
    real_crawler = Crawler(
        root_url='http://www.workopolis.com/',
        start_url='http://www.workopolis.com/content/about',
        crawl_limit=5)
    real_crawler.start_crawl()
