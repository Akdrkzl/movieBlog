from django.shortcuts import render,redirect,get_object_or_404
from .models import * 

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies,
    }
    return render(request,'index.html',context)


def movies(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies,
    }
    return render(request,'movies.html',context)

def movies_detail(request,d_slug):
    movie = Movie.objects.get(slug = d_slug)
    category_detial = movie.category.all()

    director = movie.cast.filter(cast_role__title ='Director')
    writers = movie.cast.filter(cast_role__title ='Writers')
    actor = movie.cast.filter(cast_role__title ='Actor')

    context = {
        'movie':movie,
        'category_detial':category_detial,
        'director':director,
        'writers':writers,
        'actor':actor,
    }
    return render(request,'movies-detail.html',context)


def movies_category(request,c_slug):
    category_detial = get_object_or_404(Category,slug = c_slug)
    movie = category_detial.movie_set.all()
    context = {
        'c_slug':c_slug,
        'movies':movie
    }
    return render(request,'movies-category.html',context)


def movies_favlist(request):
    if request.method == 'POST':
        slug = request.POST['favlist']
        movie = get_object_or_404(Movie, slug = slug)
        print(slug)
        print(movie)
        user_favlist,created = MovieFavList.objects.get_or_create(user = request.user)
        user_favlist.favorite_movie.add(movie)
    return redirect('index')