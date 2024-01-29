from django.shortcuts import render,get_object_or_404
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
    category = movie.category.all()

    director = movie.cast.filter(cast_role__title ='Director')
    writers = movie.cast.filter(cast_role__title ='Writers')
    actor = movie.cast.filter(cast_role__title ='Actor')

    # video_urls =[]
    # for video in movie.video_url.all():
    #     video_urls.extend([video.url_first, video.url_second, video.url_third, video.url_fourth])
    # print(video_urls)

    context = {
        'movie':movie,
        'category':category,
        'director':director,
        'writers':writers,
        'actor':actor,
    }
    return render(request,'movies-detail.html',context)