# At least three (3) class-based views
# All views are DRY with all helpers factored out to appropriate modules
# At least three database queryset methods used: all(), get(), filter()
# At least one view has additional arguments passed via url path
# All network requests have sufficient exception handling for 4xx and 5xx
# responses

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from movie_reviewer.reviews.forms import ReviewForm
from movie_reviewer.reviews.models import Review
from movie_reviewer.critics.models import Critic
from movie_reviewer.movies.models import Movie


def reviews_of_movie_view(request, movieId):
    review_html = 'reviews.html'

    current_movie = Movie.objects.get(id=movieId)
    movie_reviews = Review.objects.filter(movie=current_movie)

    professional_critics = Critics.objects.filter(professional=True)
    user_critics = Critics.objects.filter(professional=False)

    professional_reviews = Review.objects.none()
    user_reviews = Review.objects.none()

    for critic in professional_critics:
        professional_reviews = professional_reviews | movie_reviews.filter(critic=critic).first()

    for critic in user_critics:
        user_reviews = user_reviews | movie_reviews.filter(critic=critic).first()
    


    # review = Review.objects.all()
    # critic_reviews = Review.objects.filter()
    # user_reviews = Review.objects.filter()
    return render(request, review_html, {'professional_reviews': professional_reviews, 'user_reviews':user_reviews})


@login_required
def review_add_view(request, movieId):
    html = 'generic_form.html'
    movie = Movie.objects.get(id=movieId)
    critic = Critic.objects.get(pk=request.user.id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            review = Review.objects.create(
                critic = critic,
                headline = data['headline'],
                text = data['text'],
                recommend = data['recommend'],
                movie = movie
            )
            return HttpResponseRedirect(reverse('review', args=(review.id,)))
    form = ReviewForm()
    return render(request,html,{'form': form})


def delete_review(request, reviewId):
    review = Review.objects.get(pk=reviewId)
    review.delete()
    return HttpResponse('homepage')

def review_edit(request, reviewId):
    html = 'generic_form.html'
    instance = Review.objects.get(pk=reviewId)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=instance)
        form.save()
        return HttpResponseRedirect(reverse('review', args=(instance.id,)))
    form = ReviewForm(instance=instance)
    return render(request, html, {'form': form})

def review_view(request, reviewId):
    html = 'review_detail.html'
    review = Review.objects.get(pk=reviewId)
    return render(request, html,{'review': review})





