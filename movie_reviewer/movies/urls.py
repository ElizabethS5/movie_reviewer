from django.urls import path
from movie_reviewer.movies.views import (
    RecentMoviesView, MovieView, SearchMovieView, SearchResults)

urlpatterns = [
    path('', RecentMoviesView.as_view(), name='homepage'),
    path('movie/<int:id>/', MovieView.as_view(), name='movie detail'),
    path('search/', SearchMovieView.as_view(), name='search'),
    path('search_results/', SearchResults.as_view(), name='search results')
]
