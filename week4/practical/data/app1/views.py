from django.shortcuts import render


def Home(request):
    context={
        'movies':[{
            1:'Fast',
            2:'F',
            3:'Fas',
            4:'Fine'
        }]
    }
    render(request,'home.html',context)
    

# Create your views here.
