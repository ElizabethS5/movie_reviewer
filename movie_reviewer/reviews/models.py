"""At least five fields of the following list are used among all models:
BooleanField, CharField, DateField, DatetimeField, FloatField, EmailField,
TextField, URLField"""


from django.db import models
from movie_reviewer.critics.models import Critic
from movie_reviewer.movies.models import Movie
from django.utils import timezone


class Review(models.Model):
    critic = models.ForeignKey(Critic, on_delete=models.CASCADE, related_name='critic')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    headline = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(max_length=1000, null=True, blank=True)
    post_date = models.DateTimeField(default=timezone.now)
    recommend = models.BooleanField(default=True)
    critics_who_upvoted = models.ManyToManyField(Critic)


    @property
    def number_of_upvotes(self):
        return len(self.critics_who_upvoted)

    
    def __str__(self):
        return f'Review by: {self.critic} movie: {self.movie}'
