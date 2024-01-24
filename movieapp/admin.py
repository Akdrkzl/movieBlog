from django.contrib import admin
from .models import *
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


admin.site.register(Cast_Role)
admin.site.register(Cast)
admin.site.register(Category)
admin.site.register(Movie,MovieAdmin)