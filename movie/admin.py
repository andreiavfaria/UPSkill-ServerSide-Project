from django.contrib import admin
from .models import Movie, Genres

# Register your models here.
# formulario

admin.site.register(Genres)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'year', 'genres', 'image', 'actors', 'directors')
    prepopulated_fields = {'slug': ('title', 'year')}