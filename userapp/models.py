from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    user_photo = models.ImageField(upload_to='profile-photo',blank=True,null=True)
    state = models.CharField(max_length=50 ,blank=True,null=True)
    city = models.CharField(max_length=100 ,blank=True,null=True)
    zip = models.PositiveIntegerField(blank=True,null=True)
    tel = models.CharField(max_length=11 ,blank=True,null=True)