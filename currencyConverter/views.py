from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate 
from django.views import View
from .models import *
from .forms import *
from django.contrib import messages
from django.core.mail import send_mail



def index(request):
	template_name='index.html'
	form = ConversionForm(request.POST)
	return render(request, template_name, locals())

@login_required(login_url=('login'))
def AdminView(request):
	template = 'admin.html'
	countries = Country.objects.all()
	if 'addCurrency' in request.POST:
		return redirect('addCurrency')

	return render(request, template, locals())

@login_required(login_url=('login'))
def addCurrency(request):
	template = 'forms.html'
	form = CountryForm(request.POST or None, request.FILES)
	if(request.method =="POST"):
		if(form.is_valid()):
			form.save()
			return redirect('admin')
	form = CountryForm()
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
def update(request, country_id):
	country = Country.objects.get(id=country_id)

	form = CountryForm(request.POST,  instance=country)
	if(request.method == 'POST'):
		if(form.is_valid()):
			form.save()
			return redirect('admin')
	form = CountryForm(instance=country)
	return render(request, "forms.html", locals())

def about(request):
	form = ConversionForm(request.POST)
	return render(request, 'about.html', locals())

def contact(request):
	form = ConversionForm(request.POST)
	form2 = ContactForm(request.POST)
	if(request.method == 'POST'):
		if 'send' in request.POST:
			if(form2.is_valid()):
				subject = form2.cleaned_data['subject']
				message = form2.cleaned_data['message']
				from_ = form2.cleaned_data['from_']
				to_ = 'cconverter@gmail.com'
				send_mail(
				    subject,
				    message,
				    from_,
				    [to_,],
				    fail_silently=False,
				)

	return render(request, 'contact.html', locals())