import time
import datetime
import json
from hashlib import md5
from bs4 import BeautifulSoup

from PageRequest import RequestWrapper


class PageReport(object):
    def __init__(
        self, url, date,
        status_code=200,
        redirects=[],
        page_links=[]
    ):
        self.url = url
        self.id = md5(self.url).hexdigest()
        self.status_code = status_code
        self.redirects = redirects
        self.page_links = page_links
        self.date = date

    def __str__(self):
        return "Page: %s (%s) - Redirects %s" % (self.url, self.status_code, len(self.redirects))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.url == other.url

    def to_dict(self):
        return {
            "id": str(self.id),
            "url": self.url,
            # "page_links": self.page_links,
            "status_code": self.status_code,
            "redirects": len(self.redirects),
        }


class Crawler(object):
    def __init__(self, start_url, crawl_limit=5, mock_request_status=False):
        self.root_url = start_url
        self.url_queue = [start_url]
        self.crawled_urls = []
        self.crawl_limit = crawl_limit
        self.mock_request_status = mock_request_status
        self.page_reports = []

    def start(self):
        while len(self.url_queue) > 0 and len(self.crawled_urls) < self.crawl_limit:
            current_url = self.url_queue.pop(0)

            if current_url in self.crawled_urls:
                continue

            if self.outbound_link(current_url):
                print ("Skipping outbound url ", current_url)
                continue

            try:
                response = RequestWrapper(current_url, self.mock_request_status).GetRequest()
                page_soup = BeautifulSoup(response.content, 'html.parser')
            except:
                # TODO: Put malformed urls in page report
                print('Exception: Malformed URL ', current_url)

            outgoing_links = []
            for tag in page_soup.find_all('a'):
                if tag.has_attr('href'):
                    url = tag.get('href')
                    url = self.make_url_absolute_path(url, current_url)
                    outgoing_links.append(url)

            page_report = PageReport(
                url=current_url,
                date=datetime.datetime.now(),
                status_code=response.status_code,
                redirects=response.history,
                page_links=outgoing_links
            )

            print (page_report)
            self.page_reports.append(page_report)

            self.url_queue += outgoing_links
            self.crawled_urls.append(current_url)

            self.sleep()

    def sleep(self):
        time.sleep(2)

    def make_url_absolute_path(self, url, current_url):
        if url.startswith('http://') or url.startswith('https://'):
            return url

        if url.startswith('/'):
            return "http://www.workopolis.com%s" % (url)

        if current_url.endswith('/'):
            return "%s%s" % (current_url, url)
        else:
            return "%s/%s" % (current_url, url)

    def outbound_link(self, url):
        return not url.startswith(self.root_url)


if __name__ == '__main__':
    c = Crawler('http://www.workopolis.com/content/about')
    c.start()
    print json.dumps([pr.to_dict() for pr in c.page_reports])

    # d = Crawler('mysite.html', 5, True)
    # d.start()
