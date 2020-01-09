# At least three (3) class-based views
# All views are DRY with all helpers factored out to appropriate modules
# At least three database queryset methods used: all(), get(), filter()
# At least one view has additional arguments passed via url path
# All network requests have sufficient exception handling for 4xx and 5xx
# responses

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from movie_reviewer.authentication.forms import LoginForm


def login_view(request):

    html = 'generic_form.html'
    page = 'login'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
        if user:
            login(request, user)
            return HttpResponseRedirect(
                request.GET.get('next', reverse('homepage'))
            )

    form = LoginForm()
    return render(request, html, {'form': form, 'page': page})


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
