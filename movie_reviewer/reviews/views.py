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


def review_view(request, id):
    review_html = 'reviews.html'
    review = Review.objects.filter(id=id)
    return render(request, review_html, {'data': review})


@login_required
def reviewaddview(request, movieID):
    html = 'generic_form.html'

    if request.method == 'POST':
        form = reviewItemAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Review.objects.create(
                critic=request.user,
                headline=data['headline'],
                text=data['text'],
                recommend=data['recommend']
                movie=Movie.objects.get(pk=movieId)
            return HttpResponseRedirect(reverse('homepage'))

def deletereview(request):
    query = Movie.objects.get(pk=id)
    query.delete()
    return HttpResponse("Deleted!")

def edit_review_view(request, id): 
    instance = get_object_or_404(edit_reviewModel, id=id)
    form = edit_reviewForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('next_view')
    return render(request, 'edit_review_template.html', {'form': form}) 





