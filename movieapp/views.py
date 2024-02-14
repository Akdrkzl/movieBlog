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

    # try:
    #     favlist =MovieFavList.objects.get(user = request.user)
    #     favliste = favlist.favorite_movie.all()
    #     # print(favliste)
    # except MovieFavList.DoesNotExist:
    #     favliste = None

    favliste = MovieFavList.objects.filter(favorite_movie = movie, user = request.user)

    context = {
        'movie':movie,
        'category_detial':category_detial,
        'director':director,
        'writers':writers,
        'actor':actor,
        'favliste':favliste,
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
        user_favlist,created = MovieFavList.objects.get_or_create(user = request.user)
        user_favlist.favorite_movie.add(movie)
        return redirect('movies-detial', d_slug = slug)


def movies_favlist_delete(request):
    if request.method == 'POST':
        slug = request.POST['favlistslug']
        print(slug)
        movie = Movie.objects.get(slug = slug)
        print(movie)
        #birden fazla nesne içeren bir objeyi silmek istiyorsak filter ile o objeyi seçip sileriz.get kullanmak hata verir 
        fav_movie = MovieFavList.objects.filter(favorite_movie = movie)
        print(fav_movie)
        # fav_movie = get_object_or_404(MovieFavList, favorite_movie = movie)
        # print(fav_movie)
        fav_movie.delete()
        return redirect('movies-detial', d_slug = slug)