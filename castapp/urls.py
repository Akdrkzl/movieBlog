from django.urls import path
from .views import *

urlpatterns = [
    path('cast/',cast,name='cast'),
]