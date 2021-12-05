from django.urls import path
from . import views 

app_name = 'feed' 

urlpatterns = [
    path('timeline/',             views.timeline,    name="timeline"),
    path('post_detail/<str:pk>/', views.post_detail, name="post-detail"),
    path('post_update/<str:pk>/', views.post_update, name="post-update"),
    path('post_delete/<str:pk>/', views.post_delete, name="post-delete"),
    path('like_post/<str:pk>/',   views.like_post,   name="like_post"),
    path('comment/<str:pk>/',     views.comment,     name="comment"),
]