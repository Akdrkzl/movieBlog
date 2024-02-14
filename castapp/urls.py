from django.urls import path
from .views import *

urlpatterns = [
    path('cast/',cast,name='cast'),
    path('cast-detial/<str:slug>/',cast_detial,name='cast-detial'),
]