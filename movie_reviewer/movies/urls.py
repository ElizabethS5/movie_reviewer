from django.urls import path
from movie_reviewer.movies.views import (
    RecentMoviesView, MovieView, SearchMovieView, SearchResults)

urlpatterns = [
    path('', IndexView.as_view(), name='homepage')
]
