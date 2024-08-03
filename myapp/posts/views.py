from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Posts
from django.contrib.auth.decorators import login_required
from .import forms
# Create your views here.
def posts_list(request):
    posts=Posts.objects.all().order_by('-date')
    return render(request,'posts/posts_list.html',{'posts':posts}) # here {'posts':posts } is data passed as third parameter

def post_page(request,slug):
    post=Posts.objects.get(slug=slug)
    return render(request,'posts/posts_page.html',{'post':post})


@login_required(login_url="/users/login")
def post_new(request):
    if request.method=="POST":
        form=forms.CreatePost(request.POST,request.FILES)
        if form.is_valid():
            newpost=form.save(commit=False)# save with the user
            newpost.author=request.user
            newpost.save()
            return redirect('posts:list')
    form=forms.CreatePost()
    return render(request,'posts/post_new.html',{'form':form})