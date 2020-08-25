from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate 
from django.views import View
from .models import *
from .forms import *
from django.contrib import messages


def index(request):
	template_name='home.html'
	convert_form = ConvertForm(request.POST)
	if(request.method=='POST'):
		if 'submit' in request.POST:
			if(convert_form.is_valid()):
				convert = True;
				amount = convert_form.cleaned_data['amount']
				from_ = convert_form.cleaned_data['country_from']
				to_ = convert_form.cleaned_data['country_to']
				query_amount_to = Currency.objects.get(country_from = from_, country_to=to_)
				converted_amount = query_amount_to.amount_to * amount

		default_data = {'country_from':convert_form.cleaned_data['country_from'],'country_to':convert_form.cleaned_data['country_to'],'amount':convert_form.cleaned_data['amount']}
		convert_form = ConvertForm(initial=default_data)
	return render(request, template_name, locals())


def display(request):
	index.converted_amount = index.query_amount_to * int(index.amount)
	return render(request, 'display.html', locals())

@login_required(login_url=('login'))
def AdminView(request):
	currencies = Currency.objects.all()
	template = 'admin.html'
	countries = Country.objects.all()
	if 'addCountry' in request.POST:
		return redirect('addCountry')

	if 'addCurrency' in request.POST:
		return redirect('addCurency')

	return render(request, template, locals())

@login_required(login_url=('login'))
def AddCountryView(request):
	template = 'forms.html'
	country_form = CountryForm(request.POST or None, request.FILES)
	if(request.method =="POST"):
		if(country_form.is_valid()):
			country_form.save()
			return redirect('admin')
	country_form = CountryForm()
	return render(request, template, locals())

@login_required(login_url=('login'))
def AddCurrencyView(request):
	template = 'forms.html'
	currency_form = CurencyForm(request.POST or None, request.FILES)
	if(request.method =="POST"):
		if(currency_form.is_valid()):
			currency_form.save()
			return redirect('admin')
	currency_form = CurencyForm()
	return render(request, template, locals())


def disconnect(request):
	logout(request)
	return redirect("home")


def Connexion(request):
	template_name = 'forms.html'
	connexion_form = ConnexionForm(request.POST)
	if connexion_form.is_valid():
		username = connexion_form.cleaned_data['username']
		password = connexion_form.cleaned_data['password']
		user = authenticate(username=username, password=password)
		if user:  # Si l'objet renvoyé n'est pas None
			login(request, user)
			messages.success(request, "You're now connected!")
			return redirect('admin')
		else:
			messages.error(request, "logins incorrect!")
	connexion_form = ConnexionForm()
	return render(request, template_name, locals())

class Register(View):
	template_name = 'forms.html'

	def post(self, request, *args, **kwargs):
		
		register_form = RegisterForm(request.POST)
		if register_form.is_valid():
			try:
				username = register_form.cleaned_data['username']
				firstname = register_form.cleaned_data['firstname']
				lastname = register_form.cleaned_data['lastname']
				password = register_form.cleaned_data['password']
				password2 = register_form.cleaned_data['password2']
				phone = register_form.cleaned_data['phone']
				if (password == password2):
					user = User.objects.create_user(
					username=username,
					password=password)
					user.first_name, user.last_name = firstname, lastname
					user.save()
					profile = Profile(user=user, phone=phone )
					profile.save()
					messages.success(request, "Hello "+username+", you are registered successfully!")
					if user:
						login(request, user)
						return redirect("cv-admin")
				else:
					register_form = RegisterForm()
			except Exception as e:
				messages.error(request, str(e))
		register_form = RegisterForm()
		return render(request, self.template_name, locals())



@login_required(login_url='/login/')
def delete(request, currency_id):
	curency = Currency.objects.get(id=currency_id)
	curency.delete()
	return redirect('admin')


@login_required(login_url='/login/')
def update(request, currency_id):
	curency = Currency.objects.get(id=currency_id)

	update_currency_form = CurencyForm(request.POST,  instance = curency)
	if(request.method == 'POST'):
		if(update_currency_form.is_valid()):
			update_currency_form.save()
			return redirect('admin')
	update_currency_form = CurencyForm(instance=curency)
	return render(request, "forms.html", locals())