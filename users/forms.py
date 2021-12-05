from django import forms 
from django.contrib.auth.models import User 
from .models import Profile 

class EditProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields =['profile_pic','bio','location']

class EditUserForm(forms.ModelForm):
	username = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	first_name = forms.CharField(required=False)
	last_name = forms.CharField(required=False)

	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name']

	def clean_email(self):
		username = self.cleaned_data.get('username')
		email = self.cleaned_data.get('email')

		if email and User.objects.filter(email=email).exclude(username=username).count():
			raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
		return email

	