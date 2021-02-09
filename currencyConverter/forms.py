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
class ValidationForm(forms.Form):
	amount = forms.CharField(widget=forms.NumberInput(attrs={
		'placeholder':'Amount', 'class':'form-control'
		}), label='Montant recu')
	motif_validate1 =  forms.CharField(widget=forms.TextInput(attrs={
		'placeholder':'Mofif', 'class':'form-control','type':'textarea'
		}), label='Ajouter un motif', required=False)

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

	def __init__(self, *args, **kwargs):
		super(ConversionForm, self).__init__(*args, **kwargs)
		countries = Country.objects.all()
		countries = [(i.usd_value, i.name +' ('+ i.currency + ')') for i in countries]
		self.fields['country_from'] = forms.ChoiceField(
	        widget = forms.Select(attrs = {'class': 'form-control'}),
	        label = 'De la devise', choices = countries)
		self.fields['country_to'] = forms.ChoiceField(
	        widget = forms.Select(attrs = {'class': 'form-control'}),
	        label = 'A la devise', choices = countries)
		self.fields['amount'] = forms.FloatField(widget=forms.NumberInput(
			attrs={'placeholder':'Montant ','class':'form-control'}),
		label='Montant')

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


class StepForm1(forms.Form):
	amount = forms.CharField(
		widget=forms.NumberInput(attrs={
			'placeholder':'Amount', 'class':'form-control'
			}), label='Montant Saisie', required=True)
	firstname = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'placeholder':'Nom ','class':'form-control'
				}
			), label='Nom ', required=True)
	lastname = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'placeholder':'Prenom ','class':'form-control'
				}
			), label='Prenom ', required=True)
	email = forms.EmailField(
		widget=forms.TextInput(
			attrs={
				'placeholder':'Email  ','class':'form-control'
				}
			), label='Email ', required=True)

	number = forms.CharField(
		widget=forms.NumberInput(
			attrs={
				'placeholder':'Tel ','class':'form-control'
				}
			), label='Tel', required=True)

class StepForm2(forms.Form):
	firstname = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'placeholder':'Nom ','class':'form-control'
				}
			), label='Nom destinataire', required=True)
	lastname = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'placeholder':'Prenom ','class':'form-control'
				}
			), label='Prenom destinataire', required=True)
	email = forms.EmailField(
		widget=forms.TextInput(
			attrs={
				'placeholder':'Email destinataire ','class':'form-control'
				}
			), label='Email destinataire', required=True)

	number = forms.CharField(
		widget=forms.NumberInput(
			attrs={
				'placeholder':'Te. destinataire ','class':'form-control'
				}
			), label='Tel. destinataire', required=True)


class EcoCashForm(forms.Form):
	ecocash = forms.CharField(widget=forms.NumberInput(attrs={
		'placeholder':'Numero ecocash','class':'form-control','type':'number'
		}),label='Numero Ecocash', required=True)
	ecocash_holder = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder':'Numero ecocash','class':'form-control','type':'text'
		}),label='Nom detenteur compte', required=True)

class LumiCashForm(forms.Form):
	lumicash = forms.CharField(widget=forms.NumberInput(attrs={
		'placeholder':'Numero lumicash','class':'form-control','type':'number'
		}),label='Lumicash', required=True)
	lumicash_holder = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder':'Numero detenteur lumicash','class':'form-control','type':'text'
		}),label='Nom detenteur lumicash', required=True)

class LivraisonForm(forms.Form):
	tel_livraison = forms.CharField(widget=forms.NumberInput(attrs={
		'placeholder':'destinataire','class':'form-control','type':'number'
		}),label='Telephone Livraison')

class CompteForm(forms.Form):
	account_number = forms.CharField(widget=forms.TextInput(
		attrs={
			'placeholder':'','class':'form-control'
		}), label='Numéro de compte')
	account_holder = forms.CharField(widget=forms.TextInput(
		attrs={
			'placeholder':'','class':'form-control'
		}), label='Nom detenteur compte')
	bank_name = forms.CharField(widget=forms.TextInput(
		attrs={
			'placeholder':'','class':'form-control'
		}), label='Nom de la banque')
