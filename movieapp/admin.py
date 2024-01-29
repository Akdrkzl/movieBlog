from django.contrib import admin
from .models import *
# Register your models here.

class CastAdmin(admin.ModelAdmin):
    list_display = ('full_name','gender','cast_role')
    list_filter = ('gender','cast_role')
    search_fields = ('full_name','description')


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('category','language')
    search_fields = ('title','description')
    readonly_fields = ('slug',)



admin.site.register(Cast_Role)
admin.site.register(Cast,CastAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Video)
admin.site.register(Movie,MovieAdmin)