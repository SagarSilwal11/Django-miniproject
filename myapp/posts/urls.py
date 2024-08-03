from django.contrib import admin
from django.urls import path
from . import views

app_name='posts'

urlpatterns = [
    path("", views.posts_list,name="list"),
    path("new_post/", views.post_new,name="new"),
    path('<slug:slug>', views.post_page,name="page"),
]
