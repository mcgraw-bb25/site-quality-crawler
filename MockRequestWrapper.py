from RequestWrapper import RequestWrapper
import unittest




class MockRequestWrapper(RequestWrapper):

	def __init__(self, url, req_type="GET"):
		self.url = url
		self.req_type = req_type.upper()
		self.text = "</html>"
		self.content = b"</html>"

	def make_request(self):
		self.text = "<html>"
		self.content = self.text.encode()

		return self

class RequestWrapperUnitTest(unittest.TestCase):

	def test_001(self):
		mock_site = "localsite.com"
		mock_request = MockRequestWrapper(mock_site)
		mock_request.make_request()
		self.assertEqual(mock_request.text, "<html>")
		self.assertNotEqual(mock_request.text, "</html>")
		self.assertEqual(mock_request.content, b"<html>")
		self.assertNotEqual(mock_request.content, b"</html>")

if __name__ == "__main__":

	unittest.main()