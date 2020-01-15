from django.shortcuts import HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from movie_reviewer.reviews.models import Review
from movie_reviewer.critics.models import Critic
from movie_reviewer.votes.models import Vote


@login_required
def toggle_vote(request, reviewId):
    if request.user.is_staff:
        return HttpResponseRedirect(reverse('login'))
    critic = Critic.objects.get(pk=request.user.id)
    review = Review.objects.get(pk=reviewId)
    try:
        vote = Vote.objects.get(critic=critic, review=review)
        vote.delete()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    except Vote.DoesNotExist:
        Vote.objects.create(
            critic=critic,
            review=review
        )
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
