from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profil(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	phone = models.IntegerField()

class Country(models.Model):
	name = models.CharField(max_length=20)
	currency = models.CharField(max_length=20)
	usd_value = models.FloatField()

	def __str__(self):
		return f"{self.name}(1{self.currency}={self.usd_value}$)"

		

