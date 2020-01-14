# At least three (3) class-based views
# All views are DRY with all helpers factored out to appropriate modules
# At least three database queryset methods used: all(), get(), filter()
# At least one view has additional arguments passed via url path
# All network requests have sufficient exception handling for 4xx and 5xx
# responses

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from movie_reviewer.reviews.forms import ReviewForm
from movie_reviewer.reviews.models import Review
from movie_reviewer.movies.models import Movie



def reviews_of_movie_view(request, id):
    review_html = 'reviews.html'

    current_movie = Movie.objects.get(tmdb_id=id)
    movie_reviews = Review.objects.filter(movie=current_movie)

    professional_critics = Critic.objects.filter(professional=True)
    user_critics = Critic.objects.filter(professional=False)

    professional_reviews = movie_reviews.filter(
        critic__in=professional_critics, movie=current_movie)
    user_reviews = Review.objects.filter(
        critic__in=user_critics, movie=current_movie)

    # for critic in professional_critics:
    #     professional_reviews = professional_reviews | movie_reviews.filter(
    #         critic=critic).first()

    # for critic in user_critics:
    #     user_reviews = user_reviews | movie_reviews.filter(
    #         critic=critic).first()

    return render(request, review_html, {
        'professional_reviews': professional_reviews,
        'user_reviews': user_reviews,
        'movie': current_movie
    })


@login_required
def review_add_view(request, tmdb_id):
    html = 'generic_form.html'
    movie = Movie.objects.get(tmdb_id=tmdb_id)
    critic = Critic.objects.get(pk=request.user.id)
    previous_review_list = Review.objects.filter(critic=critic, movie=movie)
    if previous_review_list:
        review = previous_review_list[0]
        return review_edit(request, review.id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            review = Review.objects.create(
                critic=critic,
                headline=data['headline'],
                text=data['text'],
                recommend=data['recommend'],
                movie=movie
            )
            return HttpResponseRedirect(reverse('review', args=(review.id,)))
    form = ReviewForm()
    return render(request, html, {'form': form})


def delete_review(request, reviewId):
    review = Review.objects.get(pk=reviewId)
    review.delete()
    return HttpResponseRedirect(reverse('homepage'))


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
    user_id = request.user.id
    return render(request, html, {'review': review, 'user_id': user_id})


# def up_votes(request, id):

#     try:
#         post = Post.objects.get(id=id)
      
#     except Post.DoesNotExist():
#         return HttpResponseRedirect(reverse('homepage'))
#     post.up_votes += 1
#     post.save()
#     return HttpResponseRedirect(reverse('homepage'))
        

# def down_votes(request, id):

#     try:
#         post = Post.objects.get(id=id)
#     except Post.DoesNotExist():
#         return HttpResponseRedirect(reverse('homepage'))

#     post.down_votes += 1
#     post.save()
#     return HttpResponseRedirect(reverse('homepage'))


