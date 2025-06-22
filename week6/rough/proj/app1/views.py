from django.shortcuts import render,redirect,get_object_or_404
from .models import User

# Create your views here.
def HOME(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        email=request.POST.get("email")
        
        user=User(username=username,email=email,password=password)
        user.save()
        context={
            "username":username,
            "password":password,
            "email":email,
            "users":User.objects.all()
        }
        
        return render(request,'display.html',context)

    
    return render(request,'home.html')



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