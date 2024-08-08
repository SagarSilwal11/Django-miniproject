from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Todo
from django.contrib.auth.decorators import login_required
# Create your views here.




@login_required(login_url='login/')
def home(request):
    if request.method=='POST':
        task=request.POST.get('task')
        new_todo=Todo(user=request.user,name=task)
        new_todo.save()
    all_todos=Todo.objects.filter(user=request.user)
  
    return render(request,'todoapp/todo.html',{'context':all_todos})


def registerpage(request):
    if request.user.is_authenticated:# this code is for the user that is already login and authencticated
        return redirect('todo:home-page')
    
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        if len(password)<3:
            messages.error(request,"Password must be atleast 3 characters")
            return redirect('todo:register')
        get_all_users_by_username=User.objects.filter(username=username)
        if get_all_users_by_username:
            messages.error(request,"Username already exists")
            return redirect('todo:register')
        
        new_user=User.objects.create_user(username=username,email=email,password=password)
        new_user.save()
        messages.success(request,'User Sucessfully created,Login Now')
        return redirect('todo:login')
    return render(request,'todoapp/register.html',{})


def loginpage(request):
    if request.user.is_authenticated:# this code is for the user that is already login and authencticated
        return redirect('todo:home-page')
    if request.method=="POST":
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        
        validate_user=authenticate(username=username,password=password)
        if validate_user is not None:# check for validate user
            login(request,validate_user)
            return redirect('todo:home-page')
        else:
            messages.error(request,'Error,Please Provide the valid Credentials')
            return redirect('todo:login')
    return render(request,'todoapp/login.html',{})

@login_required(login_url='login/')
def deletetask(request,name):
    get_todo=Todo.objects.get(user=request.user,name=name)  # since the db name is give name as input parameter pass from template
    get_todo.delete()
    return redirect('todo:home-page')

@login_required(login_url='login/')
def updatetask(request,name):
    get_todo=Todo.objects.get(user=request.user,name=name)
    get_todo.status=True
    get_todo.save()
    return redirect('todo:home-page')

def logoutview(request):
    logout(request)
    return redirect('todo:login')