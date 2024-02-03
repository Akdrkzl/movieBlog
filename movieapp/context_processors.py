#Tekrarlayan yapıları bir context içerisinde yazdırabiliriz 
from .models import *

def category_context(request):
    category = Category.objects.all()
    return{'category':category}