from hashlib import md5
import datetime


class PageReport(object):
    '''
    Keeps tracks of information relating to page responses
    '''
    def __init__(
        self, url,
        status_code=200,
        redirects=[],
        page_links=[]
    ):
        self.url = url
        self.id = md5(url.encode()).hexdigest()
        self.status_code = status_code
        self.redirects = redirects
        self.page_links = page_links
        self.date = datetime.datetime.now()

    def __str__(self):
        return "Page: %s (%s)" % (self.url, self.status_code)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.url == other.url

    def get_dictionary(self):
        '''
        Returns a dictionary representation of the object
        '''
        return {
            "id": self.id,
            "url": self.url,
            "page_links": self.page_links,
            "status_code": self.status_code,
            "redirects": len(self.redirects),
        }
