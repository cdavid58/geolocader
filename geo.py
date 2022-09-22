import requests, urllib,json, pyshorteners as ps

def Locate(lat,lng):
	api_url = "https://api.opencagedata.com/geocode/v1/json?"
	key = "af0c97d90cec485b83f76a36d57c9431"
	url = api_url + urllib.parse.urlencode({'q':str(lat)+'+'+str(lng),'key':key,'pretty':1})
	response = requests.request('GET',url)
	r = json.loads(response.text)
	return r['results'][0]['components']

def Shorten_Url(url):
	return ps.Shortener().tinyurl.short(url)