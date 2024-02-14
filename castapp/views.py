from django.shortcuts import render,get_object_or_404
from .models import *

# Create your views here.
def cast(request):
    cast = Cast.objects.all()
    context = {
        'cast':cast,
    }
    return render(request,'people.html',context)

def cast_detial(request,slug):
    print(slug)
    cast = get_object_or_404(Cast , slug=slug)
    #ilgili oyuncunun ilişkili olduğu tüm filmleri bu şekilde yakalarız 
    movie = cast.movie_set.all()
    context = {
        'cast':cast,
        'movie':movie,
    }
    return render(request,'people-detail.html',context)