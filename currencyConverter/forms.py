from .models import *
from django import forms

def getValue(str_value):
	if('/' in str_value):
		splited_string = str_value.split('/')
		return float(splited_string[0])/float(splited_string[1])
	else:
		return float(str_value)

	

class ConnexionForm(forms.Form):
	username = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'placeholder':'Username ',
				'class':'form-control'
				}
			)
		)
	password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				'placeholder':'Password ',
				 'type':'password',
				 'class':'form-control'
				 }
			)
		)

class RegisterForm(forms.Form):
	username = forms.CharField( widget=forms.TextInput(
		attrs={'placeholder':'your phone number','class':'form-control'}),
		label='Phone number')
	firstname = forms.CharField( widget=forms.TextInput(
		attrs={'placeholder':'Firstname ','class':'form-control'}),
		label='Firstname')
	lastname = forms.CharField( widget=forms.TextInput(
		attrs={'placeholder':'Lastname ','class':'form-control'}),
		label='Lastname')
	password = forms.CharField( widget=forms.PasswordInput(
		attrs={'placeholder':'Password ','class':'form-control'}),
		label='Password')
	password2 = forms.CharField( widget=forms.PasswordInput(
		attrs={'placeholder':'Confirm password ','class':'form-control'}),
		label='Confirm password')

class CountryForm(forms.ModelForm):

	name = forms.CharField( widget=forms.TextInput(
		attrs={'placeholder':'Country name','class':'form-control'}),
		label='Country name'
		)
	currency = forms.CharField( widget=forms.TextInput(
		attrs={'placeholder':'Currency','class':'form-control'}),
		label='Country Code'
		)
	usd_value = forms.CharField(widget=forms.TextInput(
			attrs={'placeholder':'Country currency usd value','class':'form-control'}),
		label='USD Value'
		)

	class Meta:
		model = Country
		fields = '__all__'

class ConversionForm(forms.Form):
	country_from = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Country From', 'class': 'form-control'}),
        label = 'Country From',
        queryset = Country.objects.all())

	country_to = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Country To', 'class': 'form-control'}),
        label = 'Country To',
        queryset = Country.objects.all())

	amount = forms.FloatField(widget=forms.NumberInput(
			attrs={'placeholder':'Amount ','class':'form-control'}),
		label='Amount')

	trans_percent = TransactionPercent.objects.get(id=1)

	def __init__(self, *args, **kwargs):
		super(ConversionForm, self).__init__(*args, **kwargs)
		countries = Country.objects.all()
		countries = [(getValue(i.usd_value), i.name) for i in countries]
		self.fields['country_from'] = forms.ChoiceField(
	        widget = forms.Select(attrs = {'class': 'form-control'}),
	        label = 'Country From', choices = countries)
		self.fields['country_to'] = forms.ChoiceField(
	        widget = forms.Select(attrs = {'class': 'form-control'}),
	        label = 'Country To', choices = countries)


class ContactForm(forms.Form):
	subject = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Subject', 
                    'class': 'form-control',
                    }),
        label = 'Subject',
        )

	message = forms.CharField(
        widget = forms.Textarea(
            attrs = {'placeholder': 'Your Message', 
                    'class': 'form-control',
                    }),
        label = 'Message'
        )

	from_ = forms.EmailField(widget=forms.EmailInput(
			attrs={'placeholder':'Your Email ','class':'form-control'}),
		label='Amount',
		required=True)

