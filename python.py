'''
making web request and receving json result
'''

url = 'https://api.thisandthat.com/%s/%s/'
KEY = 'secret-api-key'

def request(noun, verb, **params):
	headers = {'apikey': KEY}
	request = urllib2.Request(url%(noun, verb),
								urllib.urlencode(params), headers)
	return json.loads(urllib2.urlopen(request).read())

