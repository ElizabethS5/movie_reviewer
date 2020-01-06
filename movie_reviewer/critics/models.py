"""At least five fields of the following list are used among all models:
BooleanField, CharField, DateField, DatetimeField, FloatField, EmailField,
TextField, URLField"""

from django.db import models
from django.contrib.auth.models import User


class Critic(User):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    displayname = models.CharField(max_length=50)
    professional = models.BooleanField()

    class Meta:
        verbose_name = 'Critic'
        verbose_name_plural = 'Critics'

    def __str__(self):
        return self.displayname
