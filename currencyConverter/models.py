from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profil(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	phone = models.IntegerField()

class Country(models.Model):
	name = models.CharField(max_length=20)
	country_currency = models.CharField(max_length=20)
	flag = models.ImageField(null=True, blank=True, upload_to='flags/')

	def __str__(self):
		return f"{self.name}({self.country_currency})"

class Currency(models.Model):
	country_from = models.ForeignKey(Country, related_name="_country_from", on_delete=models.CASCADE)
	country_to = models.ForeignKey(Country, related_name="_country_to", on_delete=models.CASCADE)
	amount_to = models.FloatField()

	def __str__(self):
		return f"{self.country_from}-{self.country_to}-{self.amount_to}"

		

