from django.shortcuts import render
from . models import MovieInfo
# Create your views here.
def create(request):
    if request.POST:
        title=request.POST.get('title')
        year=request.POST.get('year')
        movie_obj=MovieInfo(title=title,year=year)
        movie_obj.save()
    return render (request,'create.html')


def list(request):
    movie_set=MovieInfo.objects.all()
    print(movie_set)
    return render (request,'list.html',{'movies':movie_set})

def edit(request):
    return render (request,'edit.html')

    