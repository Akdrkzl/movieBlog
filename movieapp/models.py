from django.db import models
from autoslug import AutoSlugField
from castapp.models import *


# Create your models here.



class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title')


    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=50)
    url_first = models.CharField(max_length=200,blank=True)
    url_second = models.CharField(max_length=200,blank=True)
    url_third = models.CharField(max_length=200,blank=True)
    url_fourth = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.title

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    plot = models.TextField(max_length=100)
    budget = models.DecimalField(max_digits=19, decimal_places=2)
    language = models.CharField(max_length=20)
    cover_image = models.ImageField(upload_to='movie-pic')
    image = models.ImageField(upload_to='movie-pic')
    release_date = models.DateField()
    slug = AutoSlugField(populate_from='title')

    video_url = models.ManyToManyField(Video,blank=True)
    category = models.ManyToManyField(Category)
    cast = models.ManyToManyField(Cast)

    #*Admin Panelinde bulunan tekil ve çoğul isimleri değiştirir. 
    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Filmler"

    # def get_directors(self):
    #     directors = self.cast.get(is_director=True)
    #     return directors
    
    def __str__(self):
        return self.title
