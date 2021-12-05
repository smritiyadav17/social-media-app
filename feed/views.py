from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import * 
from django.contrib.auth.models import User
from .forms import *
from django.urls import reverse
from django.contrib import messages
from users.models import *

# timeline to render:create_post,show_created_post,post_detail_link
def timeline(request):
	# if method in form is POST,proceed
	if request.method == "POST":
		form = CreatePost(request.POST)
		if form.is_valid():
			content = form.cleaned_data.get('content')
			author = request.user
			post = Post()
			post.content=content
			post.author=author
			post.save()
			return redirect('feed:timeline')
	else:
		form = CreatePost()

	# latest post on top
	post = Post.objects.all().order_by('-created')
	profiles = Profile.objects.get(user=request.user)
	context ={
		'form':form,
		'post':post,
		"profiles":profiles,
	}
	return render(request, "feed/timeline.html", context)
	

def post_detail(request,pk):
	post_detail = Post.objects.get(id=pk)
	liked = False
	if post_detail.likes.filter(id=request.user.id):
		liked =True
	return render(request, "feed/post_detail.html", {'post_detail':post_detail,'liked':liked})


def post_update(request,pk):
	instance = Post.objects.get(id=pk)
	if request.method == "POST":
		form = PostUpdateForm(request.POST,instance=instance)
		if form.is_valid():
			form.save()
			messages.success(request,'Post has been created successfully!')
			return redirect('feed:timeline')
	else:
		form = PostUpdateForm(instance=instance)

	context = {"form":form,}
	return render(request, "feed/post_update.html", context)



def post_delete(request,pk):
	post_delete = Post.objects.get(id=pk)
	post_delete.delete()
	messages.success(request, "Post has been deleted successfully!")
	return redirect('feed:timeline')



def like_post(request,pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked =False 
	else:
		post.likes.add(request.user)
		liked =True 
	return HttpResponseRedirect(reverse('feed:post-detail',args=[str(pk)]))



def comment(request,pk):
	if request.method =="POST":
		post_id = request.POST.get("post_id") 
		post = Post.objects.get(id=post_id)
		user = request.user
		comment = request.POST.get("comment")
		c = Comment(post=post, user=user, comments=comment)
		c.save()
	return HttpResponseRedirect(reverse('feed:post-detail',args=[str(pk)]))