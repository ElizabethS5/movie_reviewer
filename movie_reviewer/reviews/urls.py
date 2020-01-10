from django.urls import path
from django.contrib import admin
from movie_reviewer.reviews.views import (
    review_add_view,
    reviews_of_movie_view,
    delete_review,
    review_edit, review_view)

urlpatterns = [

# path('', views.index, name='homepage'),
path('review/<int:id>',review_view, name='review'),
path('reviewadd/',review_add_view, name='reviewadd'),
path('moviereviews/<int:id>',reviews_of_movie_view, name='moviereviews'),
path('deletereview/<int:id>',delete_review, name='deletereview'),
path('reviewedit/<int:id>', review_edit, name='reviewedit')




 ]

