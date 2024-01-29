from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('movies/',movies,name='movies'),
    path('movies-detial/<str:d_slug>/',movies_detail,name='movies-detial'),
    path('movies-category/<str:c_slug>/',movies_category,name='movies-category')
]
