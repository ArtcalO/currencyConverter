from .models import *
from django import forms

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
	country_currency = forms.CharField(widget=forms.TextInput(
			attrs={'placeholder':'Country Curency ','class':'form-control'}),
		label='Country Curency'
		)

	flag = forms.ImageField(
		widget=forms.FileInput(
			attrs={'placeholder':'Country Flag','class':'form-control'}
		),
		label='Country Flag'
	)

	class Meta:
		model = Country
		fields = '__all__'

class CurencyForm(forms.ModelForm):
	country_from = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Country From', 
                    'class': 'form-control',
                    'id':'country_from'}),
        label = 'Country From',
        queryset = Country.objects.all())

	country_to = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Country To', 
                    'class': 'form-control',
                    'id':'country_from'}),
        label = 'Country To',
        queryset = Country.objects.all())

	amount_to = forms.FloatField(widget=forms.NumberInput(
			attrs={'placeholder':'Amount ','class':'form-control'}),
		label='Amount')

	class Meta:
		model = Currency
		fields = '__all__'


class ConvertForm(forms.ModelForm):
	country_from = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Country From', 
                    'class': 'form-control',
                    'id':'country_from'}),
        label = 'Country From',
        queryset = Country.objects.all())

	country_to = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Country To', 
                    'class': 'form-control',
                    'id':'country_from'}),
        label = 'Country To',
        queryset = Country.objects.all())
	amount = forms.FloatField(widget=forms.NumberInput(
			attrs={'placeholder':'Amount ','class':'form-control'}),
		label='Amount')

	class Meta:
		model = Currency
		fields = ('country_from','country_to',)
	

