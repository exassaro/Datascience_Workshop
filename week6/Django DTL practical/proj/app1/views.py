from django.shortcuts import render,redirect


# Create your views here.
def HOME(request):
    context={
        'data':[1,2,3,4,5,6,10],
        'dict':{'one':1,'two':2,'three':'3'}
    }
    return render (request,'home.html',context)
    
def NEW(request):
    return render (request,'new_page.html')