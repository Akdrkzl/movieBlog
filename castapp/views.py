from django.shortcuts import render
from .models import *

# Create your views here.
def cast(request):
    cast = Cast.objects.all()
    context = {
        'cast':cast,
    }
    return render(request,'people.html',context)