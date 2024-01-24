from django.db import models
from autoslug import AutoSlugField


# Create your models here.

class Cast_Role(models.Model):
    title = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.title

class Cast(models.Model):
    genders = (
        ('M','Male'),
        ('F','Female'),
    )

    #foreginkey ile bağlamak yerine böylede yapabiliriz 
    # cast_roles =(
    #     ('D','Director')
    #     ('W','Writers')
    #     ('A','Actor')
    #     ('S','Support')
    # )

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=50)
    image = models.ImageField(upload_to='cast-pic')
    gender = models.CharField(max_length=1, choices=genders)
    birth = models.DateField()
    location = models.CharField(max_length=50)

    cast_role = models.ForeignKey(Cast_Role, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    plot = models.TextField(max_length=100)
    budget = models.CharField(max_length=15)
    language = models.CharField(max_length=20)
    image = models.ImageField(upload_to='movie-pic')
    release_date = models.DateField()
    video = models.FileField(upload_to='movie-video')
    slug = AutoSlugField(populate_from='title')

    cast = models.ManyToManyField(Cast)

    # def get_directors(self):
    #     directors = self.cast.get(is_director=True)
    #     return directors
    
    def __str__(self):
        return self.title
