from django.db import models

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