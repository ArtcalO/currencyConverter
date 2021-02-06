from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profil(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	phone = models.IntegerField()

class Country(models.Model):
	name = models.CharField(max_length=20)
	currency = models.CharField(max_length=20)
	usd_value = models.CharField(max_length=20)

	def __str__(self):
		return f"{self.name}(1{self.currency}={self.usd_value}$)"

class TransactionPercent(models.Model):
	trans_percent = models.FloatField()

	def __str__(self):
		return f"Le taux de transaction : {self.trans_percent}"

# class Tracking(models.Model):
# 	currency_in = models.ForeignKey(Country, related_name='curr_in', on_delete=models.CASCADE)
# 	currency_out = models.ForeignKey(Country, related_name='curr_out', on_delete=models.CASCADE)
# 	amount_in = models.PositiveIntegerField()
# 	amount_out = models.PositiveIntegerField()

# 	# fielsd for sender

# 	name_sender = models.CharField(max_length=100)
# 	subname_sender = models.CharField(max_length=100)
# 	email_sender = models.EmailField()
# 	phone_sender = models.CharField(max_length=100)

# 	# fields for reciever

# 	name_reciever = models.CharField(max_length=100)
# 	subname_reciever = models.CharField(max_length=100)
# 	email_reciever = models.EmailField()
# 	phone_reciever = models.CharField(max_length=100)

# 	# Livraison 

# 	lumicash = models.IntegerField(null=True, blank=True)
# 	ecocash = models.IntegerField(null=True, blank=True)

# 	tel_livraison = models.IntegerField(null=True, blank=True)
# 	domicile_livraison = models.CharField(max_length=100, blank=True)

# 	account_number = models.IntegerField(null=True, blank=True)
# 	account_holder = models.CharField(max_length=100)
# 	bank_name = models.CharField(max_length=150)

# 	validated1 = models.BooleanField(default=False)
# 	validated2 = models.BooleanField(default=False)


# 	def __str__(self):
# 		return self.name_sender+' to '+self.name_reciever

