from django.contrib import admin
from django.urls import path,include
from . import views

app_name='todo'
urlpatterns = [
    path("",views.home,name='home-page'),
    path("register/",views.registerpage,name='register'),
    path("login/",views.loginpage,name='login'),
    path("logout/",views.logoutview,name='logout'),
    path("delete/<str:name>",views.deletetask,name='delete'),
    path("update/<str:name>",views.updatetask,name='update'),

]