from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *
# Register your models here.

class CustomUserAdmin(UserAdmin):
    # list_display=['email','first_name','last_name']
    fieldsets = UserAdmin.fieldsets + (("Kişisel Bilgiler",{"fields":["user_photo","state","city","zip","tel"]}),)
    pass

admin.site.register(CustomUser,CustomUserAdmin)