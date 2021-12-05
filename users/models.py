from django.db import models
from django.contrib.auth.models import User
from .utils import get_random_code
from django.template.defaultfilters import slugify


class Profile(models.Model):
	user        = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
	profile_pic = models.ImageField(upload_to='media/profile_pic', default='default.jpg')
	friends     = models.ManyToManyField(User, related_name="friends", null=True, blank=True)
	slug        = models.SlugField(unique=True,    null=True, blank=True)
	bio         = models.CharField(max_length=255, null=True, blank=True)
	location    = models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		return self.user.username

	def save(self, *args, **kwargs):
		ex = False 
		if self.user:
			to_slug = slugify(str(self.user))
			ex  = Profile.objects.filter(slug=to_slug).exists()
			while ex:
				to_slug = slugify(to_slug+" "+str(get_random_code))
				ex  = Profile.objects.filter(slug=to_slug).exists()
		else:
			to_slug = str(self.user)
		self.slug = to_slug
		super().save(*args,**kwargs)


	def get_friends(self):
		return self.friends.all()

	def get_friends_no(self):
		return self.friends.all().count()


class Relationship(models.Model):
	STATUS_CHOICES = (
		('send','send'),
		('accepted','accepted'),
	)
	request_sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="request_sender")
	request_receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="request_receiver")
	status = models.CharField(max_length=255, choices=STATUS_CHOICES)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.request_sender) + " - " + str(self.request_receiver) +"-" + str(self.status)
