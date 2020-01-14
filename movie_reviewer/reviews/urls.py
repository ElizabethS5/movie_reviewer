from django.urls import path
from movie_reviewer.reviews.views import (
    review_add_view,
    reviews_of_movie_view,
    delete_review,
    review_edit,
    review_view
)

urlpatterns = [
    path('review/<int:reviewId>/', review_view, name='review'),
    path('reviewadd/<int:tmdb_id>', review_add_view, name='reviewadd'),
    path('moviereviews/<int:id>', reviews_of_movie_view, name='moviereviews'),
    path('deletereview/<int:reviewId>', delete_review, name='deletereview'),
    path('reviewedit/<int:reviewId>', review_edit, name='reviewedit')
    # path('up_votes/<int:upvotesId>/', up_votes, name='upvotes'),
    # path('down_votes/<int:downvotesId>/', down_votes, name='downvotes')
]
