from requests_testadapter import Resp
import requests
import os

class LocalFileAdapter(requests.adapters.HTTPAdapter):
	'''
	Used to request local files file:///*.html

	This code is copied from 
	http://stackoverflow.com/questions/10123929/python-requests-fetch-a-file-from-a-local-url
	'''

	def build_response_from_file(self, request):
		file_path = request.url[7:]
		with open(file_path, 'rb') as file:
			buff = bytearray(os.path.getsize(file_path))
			file.readinto(buff)
			resp = Resp(buff)
			r = self.build_response(request, resp)

		return r

	def send(self, request, stream=False, timeout=None,
							verify=True, cert=None, proxies=None):

		return self.build_response_from_file(request)

if __name__ == "__main__":
	'''
	doubles as usage example
	'''
	
	requests_session = requests.session()
	requests_session.mount('file://', LocalFileAdapter())
	test_html_page = 'file://' + os.getcwd() + '/aboutus.html'
	test_html_data = requests_session.get(test_html_page)
	print (test_html_data.text)



