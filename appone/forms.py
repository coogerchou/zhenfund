from django import forms

from .models import SignUp, Transfer


class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()




class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name','email']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		
		email_base, provider = email.split('@')
		domain,extension = provider.split('.')

		#if not domain == 'zhenfund':
		#	raise forms.ValidationError('Please use zhenfund email')


		if not extension == 'edu':
			raise forms.ValidationError('Please use a valid .edu email address')
		return email

	def clean_full_name(self):
		
		full_name = self.cleaned_data.get('full_name')
		
		return full_name

class TransferForm(forms.ModelForm):

	class Meta:

		model = Transfer
		fields = ['email','original_txt'] #should this be original_txt?

	def clean_message(self):

		message = self.cleaned_data.get('message')
		return message

	def clean_email(self):

		email = self.cleaned_data.get('email')
		email_base, provider = email.split('@')
		domain,extension = provider.split('.')

		if not domain == 'zhenfund':
			raise forms.ValidationError('Please use zhenfund email')

		return email
