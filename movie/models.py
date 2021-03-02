from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from actor.models import Actor
from director.models import Director
from django.db.models import Avg
from django.urls import reverse
from django.utils import timezone


class Genres(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        pass


class Movie(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    year = models.PositiveSmallIntegerField(validators=[MaxValueValidator(2500), MinValueValidator(1800)])
    genres = models.ManyToManyField(Genres, blank=True)
    image = models.ImageField(upload_to="movie/%Y/%m/%d/", blank=True)
    rating = models.CharField(max_length=10) # tem a ver com o PG
    actors = models.ManyToManyField(Actor, blank=True)
    directors = models.ManyToManyField(Director, blank=True)

    def get_score(self):
        return self.reviews.aggregate(Avg('score'))

    def __str__(self):
        return self.title

    def get_absolute_url(self): # isto é uma função mas como está dentro de uma classe é um método
        return reverse('movie:movie_detail',
                       args=[self.id])

    class Meta:
        pass


class Review(models.Model):
    SCORE = [(i, i) for i in range(1, 11)]
    title = models.CharField(max_length=200)
    score = models.IntegerField(choices=SCORE)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews') #user.reviews
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews') #movie.reviews
    review = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = (('movie', 'user',),)
        ordering = ('created_date',)

