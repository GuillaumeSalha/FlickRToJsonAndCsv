import urllib
import urllib2
from cStringIO import StringIO
from gzip import GzipFile

class NetworkManager:
	baseUrl = ''
	headers = {"Accept":"application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5",
				"Accept-Charset":"ISO-8859-1,utf-8;q=0.7,*;q=0.3",
				"Accept-Encoding":"gzip,deflate,sdch",
				"Accept-Language":"fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4",
				"Proxy-Connection":"keep-alive",
				"User-Agent":"ComplexCity Lab, Shanghai University"}
	parameters = ''
	
	def __init__(self, userAgent, baseUrl):
		self.headers['User-Agent'] = userAgent
		self.baseUrl = baseUrl
	
	def setParameters(self, parametersDict):
		self.parameters = urllib.urlencode(parametersDict)
		
	def request(self, urlPattern):
		requestUrl = self.baseUrl + urlPattern
		request = urllib2.Request(requestUrl % self.parameters, '', self.headers)
		response = urllib2.urlopen(request)
		data = response.read()
		
		try:
			data2 = GzipFile('', 'r', 0, StringIO(data)).read()
			data = data2
		except:
			pass
		
		return data


	def requestPOST(self, urlPattern):
		self.headers = {"Accept":"application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5",
				"Accept-Charset":"ISO-8859-1,utf-8;q=0.7,*;q=0.3",
				"Accept-Encoding":"gzip,deflate,sdch",
				"Accept-Language":"fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4",
				"Proxy-Connection":"keep-alive",
				"Content-Type":"application/x-www-form-urlencoded",
				"User-Agent":"ComplexCity Lab, Shanghai University"}
		
		
		requestUrl = self.baseUrl + urlPattern
		request = urllib2.Request(requestUrl,self.parameters, self.headers)
		response = urllib2.urlopen(request)
		data = response.read()
		
		try:
			data2 = GzipFile('', 'r', 0, StringIO(data)).read()
			data = data2
		except:
			pass
		
		return data