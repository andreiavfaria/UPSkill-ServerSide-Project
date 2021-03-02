from django.contrib import admin
from .models import Movie, Genres, Review

# Register your models here.
# formulario

admin.site.register(Genres)
# admin.site.register(Review) # gera tudo como estão nos modelos


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'year', 'genres', 'image', 'actors', 'directors')
    prepopulated_fields = {'slug': ('title', 'year')}


@admin.register(Review) #
class MovieReview(admin.ModelAdmin):
    fields = ('title', 'score', 'user', 'movie', 'review')
    readonly_fields = ('user', 'movie')
