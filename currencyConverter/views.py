from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate 
from django.views import View
from .models import *
from .forms import *
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Q
from django.views.generic import ListView
from django.core.paginator import Paginator

amount_ = 0
num_receveur = 0

def splitData(data_string):
	if '/' in data_string:
		data_list = data_string.split('/')
		return float(float(data_list[0])/float(data_list[1]))
	else:
		return float(data_string)

def index(request):
	global amount_
	template_name='index.html'
	form = ConversionForm(request.POST)
	sender = Country.objects.get(name="Canada")
	reciever = Country.objects.get(name="Burundi")
	rc_value = reciever.usd_value.split('/')[1]
	if "action" in request.POST:
		if form.is_valid():
			print(form.cleaned_data)
			request.session['first_form'] = form.cleaned_data
			amount_ = form.cleaned_data['amount']
			return redirect(choice)
	if "send" in request.POST:
		amount = float(request.POST.get('inputsend'))
		data = {'country_from': sender.usd_value, 'country_to': reciever.usd_value, 'amount': amount}
		request.session['first_form'] = data
		amount_ = float(request.POST.get('inputsend'))
		return redirect(choice)

	if "recieve" in request.POST:
		amount = float(request.POST.get('inputrecieve'))
		data = {'country_from': reciever.usd_value, 'country_to': sender.usd_value, 'amount': amount}
		request.session['first_form'] = data
		amount_ = float(request.POST.get('inputrecieve'))
		return redirect(choice)

	return render(request, template_name, locals())

@login_required(login_url=('login'))
def requests(request):
	trackings = Tracking.objects.all().order_by('-id')
	paginator = Paginator(trackings, 20)
	try:
		page_number = request.GET.get('page')
	except:
		page_number = 1
	page_obj = paginator.get_page(page_number)

	return render(request, 'requests.html', {'page_obj': page_obj})

@login_required(login_url=('login'))
def validerRecu(request, id):
	track = Tracking.objects.get(id=id)
	valid_form = ValidationForm(request.POST or None, initial={'amount':track.amount_in})
	if valid_form.is_valid():
		valid = valid_form.cleaned_data
		track.amount_in_recieve = valid['amount']
		track.amount_out_deliver = float(valid['amount'])*(splitData(track.currency_in.usd_value)/splitData(track.currency_out.usd_value))
		track.motif_validate1 = valid['motif_validate1']
		track.validated1 = True
		track.save()
		return redirect(requests)
	return render(request, 'valider_modal.html', locals())

@login_required(login_url=('login'))
def validerEnvoie(request, id):
	track = Tracking.objects.get(id=id)
	track.validated2 = True
	track.save()
	return redirect(requests)
		
def choice(request):
	choice = True
	return render(request, 'steps_forms.html', locals())

def step1(request):
	global amount_
	default_data = {'amount': amount_}

	step_form1 = StepForm1(request.POST or None,initial=default_data)
	if step_form1.is_valid():
		request.session['step_form1'] = step_form1.cleaned_data
		return redirect(step2)
	return render(request, 'steps_forms.html', locals())

def step2(request):
	global num_receveur
	step_form2 = StepForm2(request.POST or None)
	if step_form2.is_valid():
		request.session['step_form2'] = step_form2.cleaned_data
		num_receveur = step_form2.cleaned_data['number']
		return redirect(step3)
	return render(request, 'steps_forms.html', locals())

def step3(request):
	choice2 = True
	global num_receveur
	data = {'num_receveur':num_receveur}
	ecocash_form=EcoCashForm(request.POST or None)
	lumicash_form=LumiCashForm(request.POST or None)
	livraison_form=LivraisonForm(request.POST or None, initial=data)
	compte_form=CompteForm(request.POST or None)

	if "ecoform" in request.POST:
		if ecocash_form.is_valid():
			eco_form = ecocash_form.cleaned_data
			first_ = request.session.pop('first_form',{})
			step_1 = request.session.pop('step_form1',{})
			print(step_1)
			step_2 = request.session.pop('step_form2',{})
			c_in = Country.objects.get(usd_value=first_['country_from'])
			c_out = Country.objects.get(usd_value=first_['country_to'])

			tracking_obj = Tracking.objects.create(
				currency_in=c_in,
				currency_out=c_out,
				amount_in=step_1['amount'],
				amount_out=float(step_1['amount'])*(splitData(c_in.usd_value)/splitData(c_out.usd_value)),


				name_sender = step_1['firstname'],
				subname_sender = step_1['lastname'],
				phone_sender = step_1['number'],

				name_reciever = step_2['firstname'],
				subname_reciever = step_2['lastname'],
				phone_reciever = step_2['number'],
				)
			tracking_obj.ecocash = eco_form['ecocash']
			tracking_obj.ecocash_holder = eco_form['ecocash_holder']
			tracking_obj.save()
			messages.success(request, "Vos informations ont été envoyées avec success. Notre équipe se charge de la suite. N'hésitez surtout pas à nous contacter sur whatsapp si vous avez des questions")
			return redirect(index)
		else:
			messages.error(request,"Une erreur de saisie est survenue, veuillez réessayer")
			return redirect(index)

	if "lumiform" in request.POST:
		if lumicash_form.is_valid():
			lumicash_data = lumicash_form.cleaned_data
			first_ = request.session.pop('first_form',{})
			step_1 = request.session.pop('step_form1',{})
			step_2 = request.session.pop('step_form2',{})
			c_in = Country.objects.get(usd_value=first_['country_from'])
			c_out = Country.objects.get(usd_value=first_['country_to'])

			tracking_obj = Tracking.objects.create(
				currency_in=c_in,
				currency_out=c_out,
				amount_in=step_1['amount'],
				amount_out=float(step_1['amount'])*(splitData(c_in.usd_value)/splitData(c_out.usd_value)),


				name_sender = step_1['firstname'],
				subname_sender = step_1['lastname'],
				phone_sender = step_1['number'],

				name_reciever = step_2['firstname'],
				subname_reciever = step_2['lastname'],
				phone_reciever = step_2['number'],
				)
			tracking_obj.lumicash = lumicash_data['lumicash']
			tracking_obj.lumicash_holder = lumicash_data['lumicash_holder']
			tracking_obj.save()
			messages.success(request, "Vos informations ont été envoyées avec success. Notre équipe se charge de la suite. N'hésitez surtout pas à nous contacter sur whatsapp si vous avez des questions")
			return redirect(index)
		else:
			messages.error(request,"Une erreur de saisie est survenue, veuillez réessayer")
			return redirect(index)

	if "receveur" in request.POST:
		if livraison_form.is_valid(): 
			livraison_data = livraison_form.cleaned_data
			first_ = request.session.pop('first_form',{})
			step_1 = request.session.pop('step_form1',{})
			step_2 = request.session.pop('step_form2',{})
			c_in = Country.objects.get(usd_value=first_['country_from'])
			c_out = Country.objects.get(usd_value=first_['country_to'])

			tracking_obj = Tracking.objects.create(
				currency_in=c_in,
				currency_out=c_out,
				amount_in=step_1['amount'],
				amount_out=float(step_1['amount'])*(splitData(c_in.usd_value)/splitData(c_out.usd_value)),


				name_sender = step_1['firstname'],
				subname_sender = step_1['lastname'],
				phone_sender = step_1['number'],

				name_reciever = step_2['firstname'],
				subname_reciever = step_2['lastname'],
				phone_reciever = step_2['number'],
				)
			tracking_obj.tel_livraison = livraison_data['num_receveur']
			tracking_obj.save()
			messages.success(request, "Vos informations ont été envoyées avec success. Notre équipe se charge de la suite. N'hésitez surtout pas à nous contacter sur whatsapp si vous avez des questions")
			return redirect(index)
		else:
			messages.error(request,"Une erreur de saisie est survenue, veuillez réessayer")
			return redirect(index)

	if "compteform" in request.POST:
		if compte_form.is_valid():
			compte_data = compte_form.cleaned_data
			first_ = request.session.pop('first_form',{})
			step_1 = request.session.pop('step_form1',{})
			step_2 = request.session.pop('step_form2',{})
			c_in = Country.objects.get(usd_value=first_['country_from'])
			c_out = Country.objects.get(usd_value=first_['country_to'])

			tracking_obj = Tracking.objects.create(
				currency_in=c_in,
				currency_out=c_out,
				amount_in=step_1['amount'],
				amount_out=float(step_1['amount'])*(splitData(c_in.usd_value)/splitData(c_out.usd_value)),


				name_sender = step_1['firstname'],
				subname_sender = step_1['lastname'],
				phone_sender = step_1['number'],

				name_reciever = step_2['firstname'],
				subname_reciever = step_2['lastname'],
				phone_reciever = step_2['number'],
				)
			
			tracking_obj.account_number = compte_data['account_number']
			tracking_obj.account_holder = compte_data['account_holder']
			tracking_obj.bank_name = compte_data['bank_name']
			tracking_obj.save()
			messages.success(request, "Vos informations ont été envoyées avec success. Notre équipe se charge de la suite. N'hésitez surtout pas à nous contacter sur whatsapp si vous avez des questions")
			return redirect(index)
		else:
			messages.error(request,"Une erreur de saisie est survenue, veuillez réessayer")
			return redirect(index)
	return render(request, 'steps_forms.html', locals())

@login_required(login_url=('login'))
def AdminView(request):
	adm = True
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
			messages.error(request,request, "logins incorrect!")
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
					profile = Profile(user=user, phone=phone)
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
	if "action" in request.POST:
		if form.is_valid():
			request.session['first_form'] = form.cleaned_data
			return redirect(choice)
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
