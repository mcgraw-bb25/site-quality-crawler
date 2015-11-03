

from RequestWrapper import RequestWrapper
from MockRequestWrapper import MockRequestWrapper

class Crawler(RequestWrapper):

	def __init__(self, url):
		self.url = url

	def crawl(self):
		super().__init__(self.url)
		print ("Hitting %s url" % (self.url))
		response = super().make_request()
		print (response.text[0:50])


class MockCrawler(Crawler, MockRequestWrapper):
	pass


if __name__ == "__main__":
	c = Crawler("http://www.workopolis.com")
	c.crawl()

	d = MockCrawler("notrealsite.com")
	d.crawl()
