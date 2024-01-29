from django.shortcuts import render,get_object_or_404
from .models import * 

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    category = Category.objects.all()

    context = {
        'movies':movies,
        'category':category,
    }
    return render(request,'index.html',context)


def movies(request):
    movies = Movie.objects.all()
    category = Category.objects.all()


    context = {
        'movies':movies,
        'category':category,
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


def movies_category(request,c_slug):

    category = Category.objects.all()

    category_detial = get_object_or_404(Category,slug = c_slug)
    movie = category_detial.movie_set.all()

    print(f'/movies-category/{c_slug}/')
    
    context = {
        'c_slug':c_slug,
        'category':category,
        'movies':movie
    }
    return render(request,'movies-category.html',context)