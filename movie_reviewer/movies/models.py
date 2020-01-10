"""At least five fields of the following list are used among all models:
BooleanField, CharField, DateField, DatetimeField, FloatField, EmailField,
TextField, URLField"""

from django.db import models
# from django.utils import timezone


class Movie(models.Model):
    title = models.CharField(max_length=200)
    imdb_id = models.CharField(max_length=200)
    overview = models.CharField(max_length=2000)
    poster_path = models.CharField(max_length=200)
    release_date = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} imdbID: {self.imdb_id} (id: {self.id})"
