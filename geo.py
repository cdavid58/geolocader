import requests, urllib,json, pyshorteners as ps
from geopy.geocoders import Nominatim

def Locate(lat,lng):
	api_url = "https://api.opencagedata.com/geocode/v1/json?"
	key = "af0c97d90cec485b83f76a36d57c9431"
	url = api_url + urllib.parse.urlencode({'q':str(lat)+'+'+str(lng),'key':key,'pretty':1})
	response = requests.request('GET',url)
	r = json.loads(response.text)
	return r['results'][0]['components']

def Shorten_Url(url):
	return ps.Shortener().tinyurl.short(url)


def Locate_(coord):
	lat,lng = coord.split(',')
	lat = float(lat)
	lng = float(lng)
	coord = str(lat)+','+str(lng)
	api_url = "http://api.positionstack.com/v1/reverse?"
	key = "07e29500b5177580d04a091628600602"
	url = api_url + urllib.parse.urlencode({'access_key':key,'query':coord,'output':'json','limit':1})
	response = requests.request('GET',url)
	r = json.loads(response.text)
	return r

# https://www.openstreetmap.org/export/embed.html?bbox=lng,lat,lng,lat&layer=mapnik&marker=lat,lng
#75.535823

# location = geolocator.reverse("6.228967, -75.535823")