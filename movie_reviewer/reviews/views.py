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

def index(request):
    html = 'index.html'
    reviews = Review.objects.all()
    return render(request, html, {'data': reviews})


def review_view(request, id):
    review_html = 'reviews.html'
    review = Review.objects.filter(id=id)
    return render(request, review_html, {'data': review})


@login_required
def reviewaddview(request):
    html = 'generic_form.html'

    if request.method == 'POST':
        form = reviewItemAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ReviewItem.objects.create(
                critic=request.user,
                title=data['title'],
                text=data['text'],
                recommend=data['recommend']
            )
            return HttpResponseRedirect(reverse('homepage'))
   





