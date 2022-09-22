from django.db import models
from locate.models import User

class Token(models.Model):
	token = models.CharField(max_length = 96)


class Victim(models.Model):
	name = models.CharField(max_length = 40)
	phone = models.CharField(max_length = 25,unique= True)
	redirect = models.IntegerField()
	user = models.ForeignKey(User,on_delete = models.CASCADE)

class History(models.Model):
	city = models.CharField(max_length=80)
	city_district = models.CharField(max_length = 150)
	country = models.CharField(max_length=80)
	road = models.CharField(max_length = 150)
	state = models.CharField(max_length = 100)
	state_district = models.CharField(max_length = 250)
	suburb = models.TextField()
	lat = models.CharField(max_length=150,blank = True)
	lng = models.CharField(max_length=150,blank = True)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	victim = models.ForeignKey(Victim,on_delete=models.CASCADE,blank=True)
	search_date = models.DateField(auto_now= True)

	def __str__(self):
		return self.user.email



