from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^$',Home,name="Home"),
	url(r'^Dashboard/$',Dashboard,name="Dashboard"),
]