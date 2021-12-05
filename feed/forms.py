from django import forms 
from .models import *

class PostUpdateForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['content']


class CreatePost(forms.ModelForm):
	
	class Meta:
		model = Post 
		fields  = ['content']
