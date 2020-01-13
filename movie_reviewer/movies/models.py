"""At least five fields of the following list are used among all models:
BooleanField, CharField, DateField, DatetimeField, FloatField, EmailField,
TextField, URLField"""

from django.db import models
from django.apps import apps


class Movie(models.Model):
    title = models.CharField(max_length=200)
    tmdb_id = models.CharField(max_length=200)
    overview = models.CharField(max_length=2000)
    poster_path = models.CharField(max_length=200)
    release_date = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} tmdbID: {self.tmdb_id})"

    @property
    def get_cumultive_recommend_percentage(self):
        Review = apps.get_model(
            app_label='movie_reviewer', model_name='Review')
        reviews = Review.objects.filter(movie=self)
        if not reviews:
            return None
        positive_reviews = [review for review in reviews if review.recommend]
        return round((len(positive_reviews) / len(reviews) * 100), 1)

    @property
    def get_professional_recommend_percentage(self):
        Review = apps.get_model(
            app_label='movie_reviewer', model_name='Review')
        reviews = Review.objects.filter(movie=self)
        if not reviews:
            return None
        pro_reviews = [
            review for review in reviews if review.critic.professional]
        if not pro_reviews:
            return None
        positive_pro_reviews = [
            review for review in pro_reviews if review.recommend]
        return round((len(positive_pro_reviews) / len(pro_reviews) * 100), 1)

    @property
    def get_audience_recommend_percentage(self):
        Review = apps.get_model(
            app_label='movie_reviewer', model_name='Review')
        reviews = Review.objects.filter(movie=self)
        if not reviews:
            return None
        audience_reviews = [
            review for review in reviews if not review.critic.professional]
        if not audience_reviews:
            return None
        positive_audience_reviews = [
            review for review in audience_reviews if review.recommend]
        return round(
            (len(positive_audience_reviews) / len(audience_reviews) * 100), 1
        )
