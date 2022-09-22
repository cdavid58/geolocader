from django.http import HttpResponse
from django.shortcuts import render,redirect
import requests, json
from geo import Locate
from .models import User


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def Home(request):
	if request.method == 'POST':
		try:
			user = User.objects.get(email = request.POST.get('email'),pswd = request.POST.get('pass'))
			request.session['username'] = user.username
			request.session['pk_user'] = user.pk
			return redirect('Dashboard')
		except User.DoesNotExist:
			pass
	# url = "http://ip-api.com/json/191.95.39.31"
	# data = {}
	# headers = {
 #      'Content-Type': 'application/json',
 #      'Accept': 'application/json'
 #    }
	# response = requests.request('GET',url,headers = headers, data = data)
	# resp = json.loads(response.text)
	# lat = resp['lat']
	# lng = resp['lon']
	# print(Locate(lat,lng))
	# return HttpResponse(resp)

	return render(request,'login.html')

def Dashboard(request):
	return render(request,'index.html')
