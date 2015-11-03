from RequestWrapper import RequestWrapper
import unittest

class MockResponseObject(object):

	def __init__(self, text, content):
		self.text = text
		self.content = content

class MockRequestWrapper(RequestWrapper):

	def __init__(self, url, req_type="GET"):
		self.url = url
		self.req_type = req_type.upper()
		self.text = "</html>"
		self.content = b"</html>"

	def make_request(self):
		self.text = "<html>"
		self.content = self.text.encode()

		response = MockResponseObject(self.text, self.content)

		return response

class RequestWrapperUnitTest(unittest.TestCase):

	def test_001(self):
		mock_site = "localsite.com"
		mock_request = MockRequestWrapper(mock_site).make_request()
		# mock_request.make_request()
		self.assertEqual(mock_request.text, "<html>")
		self.assertNotEqual(mock_request.text, "</html>")
		self.assertEqual(mock_request.content, b"<html>")
		self.assertNotEqual(mock_request.content, b"</html>")

if __name__ == "__main__":

	unittest.main()