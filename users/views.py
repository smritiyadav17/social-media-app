from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from feed.urls import *

def signup(request):
	if request.method=="POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f'Account has been created successfully for {username}!')
			login(request,user)
			return redirect('login')
	else:
		form = UserCreationForm()
	return render(request, "users/signup.html", {'form':form})


def edit_profile(request,pk):
	get_connection = Profile.objects.get(user=request.user)
	instance = User.objects.get(id=pk)
	profile_instance = Profile.objects.get(user=instance)
	if request.method == "POST":
		form = EditUserForm(request.POST, instance=instance)
		profile_form = EditProfileForm(request.POST, request.FILES, instance= profile_instance)
		if form.is_valid() and profile_form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			profile_form.save()
			messages.success(request,f'Changes have been saved for {username}!')
			return redirect('feed:timeline')
		else:
			form = EditUserForm(instance=instance)
			profile_form = EditProfileForm(instance=profile_instance)


	return render(request, "users/edit_profile.html", {"get_connection":get_connection} )

	# return render(request, "users/edit_profile.html", {'form':form,'profile_form':profile_form,"get_connection":get_connection} )
