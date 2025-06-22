from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    movie_data= {
       "movies":[{
        'title':'Godfather',
        'year':'1990',
        'Success': True
    },
    {
        'title':'Titanic',
        'year':'1999',
        'Success': True
    }
     ,
    {
        'title':'Bee',
        'year':'2005',
        'Success': False
    },
    {
        'title':'Thing',
        'year':'2016',
        'Success': True
    },
    {
        'title':'Fan',
        'Success': False
    }
    ]}
   
    return render(request,'hello.html',movie_data)
    