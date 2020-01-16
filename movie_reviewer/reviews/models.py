"""At least five fields of the following list are used among all models:
BooleanField, CharField, DateField, DatetimeField, FloatField, EmailField,
TextField, URLField"""


from django.db import models
from movie_reviewer.critics.models import Critic
from movie_reviewer.movies.models import Movie
from django.utils import timezone
from django.apps import apps


class Review(models.Model):
    critic = models.ForeignKey(Critic, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    headline = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(max_length=1000, null=True, blank=True)
    post_date = models.DateTimeField(default=timezone.now)
    recommend = models.BooleanField(default=True)

    def __str__(self):
        return f'Review by: {self.critic} movie: {self.movie}'

    @property
    def vote_number(self):
        Vote = apps.get_model(
            app_label='movie_reviewer', model_name='Vote')
        votes = Vote.objects.filter(review=self)
        return len(votes)

    @property
    def voter_list(self):
        Vote = apps.get_model(
            app_label='movie_reviewer', model_name='Vote')
        votes = Vote.objects.filter(review=self)
        voters = [vote.critic for vote in votes]
        return voters
