from django.shortcuts import render
from .models import User

# Create your views here.
def HOME(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        
        user = User(username=username,password=password,email=email)
        
        user.save()
        
        context={
            "message":"User data has been saved successfully",
            "username": username,
            "email" : email,
            "users" : User.objects.all(),
            
            }
        return render(request,'display.html',context)
    return render(request,'home.html')