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

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.TextField(max_length=50)
    image = models.ImageField(upload_to='cast-pic')
    gender = models.CharField("Cinsiyet",max_length=1, choices=genders)
    birth = models.DateField()
    location = models.CharField(max_length=50)

    cast_role = models.ForeignKey(Cast_Role, on_delete = models.CASCADE,verbose_name='Görev')

    #*burada isim ve soyisimi birleştirip admin panelinde full_name'i çağırıp kullanabiliriz
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"   

    #*Admin panelindeki kısa açıklamayı değiştirdik 
    full_name.fget.short_description = 'Ad Soyad'

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.cast_role})"

class Category(models.Model):
    title = models.CharField(max_length=50)

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
