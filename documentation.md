Project = Social Media (Postshare Site)


Structure:
	project/
			users (app)
				-register
				-login
				-Profile (OneToOne:User)
					-Edit Profile
				-Relationship (ForiegnKey:Profile)
					-Add Friends

			feed (app)
				-Create post
				-Edit Post 
				-Delete Post 
				-Like Post 
				-Comment



Pointers/Steps about the Project:

1.pip install django 
2.django-admin startproject project
3.After creating our project, we move on to create our frist app "users"
4.cd project
5.python manage.py startapp users 
6.Now that our "users" app has been created, we'll add it in our project's settings.py file's INSTALLED_APPS
7.Next we will create a "Profile" model, which will link User to their one profile, and will be created 
	automatically by using "signals".
8.Once, on creating our user, thier profile get created..we make "edit_profile" view to allow users 
	to edit/add details, and redirect them to timeline
9.then we need other users to connect to and share our content, we make "Relationship" table,
	which connects registered users 

	Note:Relationship works from "admin.py" but the frontend and logic part for Add-friend/Send-Request/Accept-Request has not been created yet.	(*working on it)

10.Now that we've created our users and its basic functionality, we can go on to create our posts
	for which we'll create our feed app
11.python manage.py startapp feed 
	Feed
		/models.py
			/Post
			/Comment

12.We create "Post" and "Comment" table, and make CRUD for the same 
	Post(views.py and urls.py)
		/timeline     			 #show all posts
		/post_detail/<str:pk>/	 
					/like_post   
					/comment

		#allow only respective authors to modify
		post_update/<str:pk>/
		post_delete/<str:pk>/

13.Other libraries such as :
	-crispy forms 
	-python decouple 
has been installed to improve the look and security feature of the application!




Overview of Project:
-This project has been built by me using django web framework, it is made for practice purpose!
-The application allows users to register themselves and log in their account.
-Update or modify their profile data, set profile picture,etc
-Can add other registered users to their friend list 
-Can share the post,edit,delete,like and comment on other users shared content!
-Users can logout and gets redirected to the signup page!


Endpoints:
	Users:
		http://127.0.0.1:8000/signup/
		http://127.0.0.1:8000/login/
		http://127.0.0.1:8000/logout/
		http://127.0.0.1:8000/edit_profile/1

	Feed:
		http://127.0.0.1:8000/timeline
		http://127.0.0.1:8000/post_detail/pk
		http://127.0.0.1:8000/post_update/pk
		http://127.0.0.1:8000/post_delete/pk
		http://127.0.0.1:8000/like_post/pk
		http://127.0.0.1:8000/comment/pk

