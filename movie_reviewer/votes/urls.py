from django.urls import path
from movie_reviewer.votes.views import toggle_vote

urlpatterns = [
    path('vote/<int:reviewId>', toggle_vote, name='vote'),
]
