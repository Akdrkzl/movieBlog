from django.shortcuts import render
from .models import * 

# Create your views here.
def index(request):
    movies = Movie.objects.all()

    context = {
        'movies':movies
    }
    return render(request,'index.html',context)


def movies(request):
    movies = Movie.objects.all()

    context = {
        'movies':movies
    }
    return render(request,'movies.html',context)

def movies_detail(request,d_slug):

    movie = Movie.objects.get(slug = d_slug)

    director = movie.cast.filter(cast_role__title ='Director')
    writers = movie.cast.filter(cast_role__title ='Writers')
    actor = movie.cast.filter(cast_role__title ='Actor')

    print(director)
    context = {
        'movie':movie,
        'director':director,
        'writers':writers,
        'actor':actor
    }
    return render(request,'movies-detail.html',context)