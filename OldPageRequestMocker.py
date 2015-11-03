import requests
import os

from mockrequests import LocalFileAdapter

class RequestWrapper(object):

	def __init__(self, url, mock_request_status = False):
		self.url = url
		self.mock_request_status = mock_request_status

	def GetRequest(self):
		if self.mock_request_status == False:
			return requests.get(self.url)
		else:
			requests_session = requests.session()
			requests_session.mount('file://', LocalFileAdapter())
			test_html_page = 'file://' + os.getcwd() + '/' + self.url
			test_html_data = requests_session.get(test_html_page)
			return test_html_data

if __name__ == "__main__":

	real_site = 'http://www.workopolis.com'
	real_site_test_status = False
	real_request = RequestWrapper(real_site, real_site_test_status).GetRequest()
	print (real_request.text[:500])

	test_site = 'aboutus.html'
	test_site_test_status = True
	test_request = RequestWrapper(test_site, test_site_test_status).GetRequest()
	print (test_request.content[0:500])

