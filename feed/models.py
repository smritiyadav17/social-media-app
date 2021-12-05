from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 

class Post(models.Model):
	content = models.TextField() 
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	author  = models.ForeignKey(User,related_name='post' ,on_delete=models.CASCADE)
	slug    = models.SlugField() 
	likes   = models.ManyToManyField(User, related_name='blog_post', null=True, blank=True)
	
	def __str__(self):
		return  str(self.content[:100])

class Comment(models.Model):
	post = models.ForeignKey(Post, related_name="comments",on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	dt_posted = models.DateTimeField(auto_now=True)
	comments = models.TextField()
	parent = models.ForeignKey('self',max_length=255, on_delete=models.CASCADE,null=True,blank=True) 

	def __str__(self):
		return str(self.id) 
