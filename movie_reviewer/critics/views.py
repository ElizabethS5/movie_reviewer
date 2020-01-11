# At least three (3) class-based views
# All views are DRY with all helpers factored out to appropriate modules
# At least three database queryset methods used: all(), get(), filter()
# At least one view has additional arguments passed via url path
# All network requests have sufficient exception handling for 4xx and 5xx
# responses


from django.shortcuts import HttpResponseRedirect, reverse  # render
from django.contrib.auth import login
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from movie_reviewer.critics.forms import NewCriticForm
from movie_reviewer.critics.models import Critic
from movie_reviewer.reviews.models import Review


class CreateCritic(CreateView):
    template_name = 'generic_form.html'
    form_class = NewCriticForm

    def form_valid(self, form):
        data = form.cleaned_data
        critic = Critic.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            displayname=data['displayname'],
            professional=data['professional']
        )
        login(self.request, critic)
        return HttpResponseRedirect(reverse('homepage'))


class CriticView(DetailView):
    model = Critic
    template_name = 'critic_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(critic=self.get_object())
        return context


class CriticListView(ListView):
    model = Critic
    paginate_by = 100
    template_name = 'critic_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        return super().get_context_data(**kwargs)
