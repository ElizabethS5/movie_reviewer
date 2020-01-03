from django.urls import path
from movie_reviewer.movies.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='homepage')
]
