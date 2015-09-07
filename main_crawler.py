import time
import datetime
import requests
from bs4 import BeautifulSoup

class Crawler(object):

	def __init__(self):
		self.to_crawl = []
		self.have_crawled = []
		self.pages_to_crawl = 20 # CLI arg
		self.key_url_root = 'http://www.workopolis.com' # CLI arg

	def addCrawledPage(self, newpage):
		if newpage not in self.have_crawled:
			self.have_crawled.append(newpage)
			return True
		return False

	def addPageToCrawl(self, newpage):
		if newpage not in self.to_crawl and self.key_url_root in newpage.url:
			self.to_crawl.append(newpage)
			#print("Page added: ", newpage.url)

	def startCrawl(self, startpage):
		# consume page
		# add all the links
		# crawl next page

		self.addPageToCrawl(startpage)
		page_counter = 0
		while self.to_crawl and page_counter <= self.pages_to_crawl:
			time.sleep(3)
			nextPage = self.to_crawl.pop(0)
			page_counter = page_counter + 1
			
			if self.addCrawledPage(nextPage):
				urls = self.getPageLinks(nextPage)

				for url in urls:
					newPage = Page(url)
					self.addPageToCrawl(newPage)

				self.addCrawledPage(nextPage)
			for link in self.to_crawl:
				print (link.url)
			nextPage.printPageData()


	def getPageLinks(self, page):
		'''
		add defintions and such
		'''


		urls = []
		try:
			page_response = requests.get(url = page.url)
			if page_response.content:
				page.statuscode = page_response.status_code
				page.redirects = page_response.history
				soup = BeautifulSoup(page_response.content, 'html.parser')
				for link in soup.find_all('a'):
					link = str(link.get('href'))
					urls.append(link)

			page.to_links = urls

		except:
			print('Bad url found here:', page.url)

		return urls
		
	def printAllPageData(self):
		'''
		Prints page metrics
		'''

		'''
		print ('Pages left --')
		for page in self.to_crawl:
			print (page.url)

		print ('Pages crawled --')
		for page in self.have_crawled:
			print (page.url)
			print ('links')
			for url in page.to_links:
				print (url)
		'''
		pass



class CrawlerTest(object):

	def __init__(self):
		self.crawler = Crawler()

	def testAddCrawledPage(self):
		startPage = Page('http://www.workopolis.com')
		pageOne = Page('http://www.workopolis.com/newpage/')
		pageTwo = Page('http://www.workopolis.com')
		self.crawler.addCrawledPage(startPage)
		assert self.crawler.have_crawled == [Page('http://www.workopolis.com')]
		self.crawler.addCrawledPage(pageOne)
		assert self.crawler.have_crawled == [Page('http://www.workopolis.com'), Page('http://www.workopolis.com/newpage/')]
		self.crawler.addCrawledPage(pageTwo)
		assert self.crawler.have_crawled == [Page('http://www.workopolis.com'), Page('http://www.workopolis.com/newpage/')]

	##### test other page adder later when Mat B isn't in the same country as me!!!!!

class Page(object):

	def __init__(self, url):
		self.url = url
		self.statuscode = None
		self.redirects = []
		self.to_links = []

	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.url == other.url
		else:
			return False

	def printPageData(self):

		print ('URL:', self.url, ' at ', datetime.datetime.now(), ' Status: ', self.statuscode, ' Redirects: ', len(self.redirects))

#### To Do Section ####
'''
1) Writing data to JSON objects -> building out the reporting model.
2) Adding relative links
3) Building Site class to understand all links in total, like a dict


'''



if __name__ == '__main__':

	newCrawlerTest = CrawlerTest()
	newCrawlerTest.testAddCrawledPage()

	startpage = Page('http://www.workopolis.com/content/about')
	newCrawler = Crawler()
	newCrawler.startCrawl(startpage)
	#newCrawler.printAllPages()