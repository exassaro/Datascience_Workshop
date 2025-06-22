from django.shortcuts import render,redirect,get_object_or_404
from .models import User
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method=="POST":
        messages.success(request,"Form submitted sucessfully!")
        username=request.POST.get("username")
        password=request.POST.get("password")
        email=request.POST.get("email")
        
        user=User(username=username,email=email,password=password)
        user.save()     
        
        request.session['username']=username
        # to get current username
        return redirect('display')
    return  render(request,'home.html')

def display(request):
    username=request.session.get('username',None)  #username to show get here
    users=User.objects.all()
    return render(request,'display.html',{ 'users':users, 'username': username })

def update(request,user_id):
    user=get_object_or_404(User,id=user_id)
    if request.method=="POST":
        user.username=request.POST.get("username",user.username)
        user.password=request.POST.get("password",user.password)
        user.email=request.POST.get("email",user.email)
        user.save()
        return redirect('display')
    
    return render(request,'update.html',{'user':user})


def delete(request,user_id):
    user=get_object_or_404(User,id=user_id)
    user.delete()
    return redirect('display')
        
        
        
