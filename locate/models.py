from django.db import models

class User(models.Model):
	username = models.CharField(max_length=30)
	email = models.EmailField()
	phone = models.CharField(max_length=25)
	block = models.BooleanField(default= False)
	pswd = models.CharField(max_length=20,blank = True)
	search_limit = models.IntegerField(default= 3)



class Location(models.Model):
	city = models.CharField(max_length=80)
	city_district = models.CharField(max_length = 150)
	country = models.CharField(max_length=80)
	road = models.CharField(max_length = 150)
	state = models.CharField(max_length = 100)
	state_district = models.CharField(max_length = 250)
	suburb = models.TextField()
	user = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.user.email

