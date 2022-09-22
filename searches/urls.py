from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Search_By_Link/$',Search_By_Link,name="Search_By_Link"),
	url(r'^register_information/(\w+)/(\w+)/(\w+)/$',Capture_Data,name="register_information"),
	url(r'^Search_History/$',Search_History,name="Search_History"),
]