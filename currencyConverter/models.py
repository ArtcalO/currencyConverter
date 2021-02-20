from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
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


class Tracking(models.Model):
	currency_in = models.ForeignKey(Country, related_name='curr_in', on_delete=models.CASCADE)
	currency_out = models.ForeignKey(Country, related_name='curr_out', on_delete=models.CASCADE)
	amount_in = models.FloatField()
	amount_out = models.FloatField()
	amount_in_recieve = models.FloatField(null=True)
	amount_out_deliver = models.FloatField(null=True)

	# fielsd for sender

	name_sender = models.CharField(max_length=100)
	subname_sender = models.CharField(max_length=100)
	phone_sender = models.CharField(max_length=100)

	# fields for reciever

	name_reciever = models.CharField(max_length=100)
	subname_reciever = models.CharField(max_length=100)
	phone_reciever = models.CharField(max_length=100)

	# Livraison 

	lumicash = models.FloatField(null=True, blank=True)
	lumicash_holder = models.CharField(max_length=100)
	ecocash = models.FloatField(null=True, blank=True)
	ecocash_holder = models.CharField(max_length=100)

	tel_livraison = models.IntegerField(null=True, blank=True)

	account_number = models.IntegerField(null=True, blank=True)
	account_holder = models.CharField(max_length=100)
	bank_name = models.CharField(max_length=150)

	validated1 = models.BooleanField(default=False)
	motif_validated1 = models.TextField(blank=True, null=True, default='Rien')
	validated2 = models.BooleanField(default=False)

	date = models.DateField(default=timezone.now)


	def __str__(self):
		return self.name_sender+' to '+self.name_reciever

	def senderFullName(self):
		return self.name_sender+' '+self.subname_sender

	def recieverFullName(self):
		return self.name_reciever+' '+self.subname_reciever

	def montantDepart(self):
		return f"{self.amount_in} {self.currency_in.currency}"

	def montantRecuAdmin(self):
		return f"{self.amount_in_recieve} {self.currency_in.currency}"

	def montantArriveAdmin(self):
		return f"{self.amount_out_deliver} {self.currency_out.currency}"

	def montantArrive(self):
		return f"{self.amount_out} {self.currency_out.currency}"

			



