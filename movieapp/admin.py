from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('category','language')
    search_fields = ('title','description')
    readonly_fields = ('slug',)

class MovieFavListAdmin(admin.ModelAdmin):
    list_display = ('user','get_favlist')
    
    def get_favlist(self,obj):
        return "\n".join([movie.title for movie in obj.favorite_movie.all()])
    

admin.site.register(Category,CategoryAdmin)
admin.site.register(Video)
admin.site.register(Movie,MovieAdmin)
admin.site.register(MovieFavList,MovieFavListAdmin)