"""At least five fields of the following list are used among all models:
BooleanField, CharField, DateField, DatetimeField, FloatField, EmailField,
TextField, URLField"""


from django.db import models
from movie_reviewer.critics.models import Critic
from movie_reviewer.movies.models import Movie
from django.utils import timezone


class Review(models.Model):
    critic = models.ForeignKey(Critic, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    post_date = models.DateTimeField(default=timezone.now)
    recommend = models.BooleanField(default=True)


    def _str_(self):
        return self.headline


