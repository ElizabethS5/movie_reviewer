from django.db import models
from movie_reviewer.critics.models import Critic
from movie_reviewer.reviews.models import Review


class Vote(models.Model):
    critic = models.ForeignKey(Critic, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
