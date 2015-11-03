import requests
import unittest

class RequestTypeError(Exception):
	pass

class RequestWrapper(object):

	def __init__(self, url, req_type = "GET"):
		self.url = url
		self.req_type = req_type.upper()

	def make_request(self):
		if self.req_type == "GET":
			response = requests.get(self.url)
		elif self.req_type == "POST":
			response = requests.post(self.url)
		else:
			raise RequestTypeError("ERROR - Invalid request type")

		return response


class RequestWrapperUnitTest(unittest.TestCase):

	def test_001(self):
		real_site = 'https://duckduckgo.com'
		real_request = RequestWrapper(real_site).make_request()
		self.assertIsNotNone(real_request.text)

	def test_002(self):
		real_site = 'https://duckduckgo.com'
		request = RequestWrapper(real_site, "ZZZ")
		self.assertRaises(RequestTypeError, request.make_request)

	def test_003(self):
		real_site = 'https://duckduckgo.com'
		real_request = RequestWrapper(real_site,"get").make_request()
		self.assertIsNotNone(real_request.text)

if __name__ == "__main__":

	unittest.main()