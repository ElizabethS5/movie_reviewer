from django.urls import path
from movie_reviewer.movies.views import *

urlpatterns = [
    path('', RecentMoviesView.as_view(), name='homepage'),
    path('movie/<int:id>/', MovieView.as_view(), name='movie detail')
]
