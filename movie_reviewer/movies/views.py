# At least three (3) class-based views
# All views are DRY with all helpers factored out to appropriate modules
# At least three database queryset methods used: all(), get(), filter()
# At least one view has additional arguments passed via url path
# All network requests have sufficient exception handling for 4xx and 5xx
# responses

# , HttpResponseRedirect, reverse
# from django.contrib.auth import login
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
# import re
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from movie_reviewer.movies.forms import SearchForm
from movie_reviewer.movies.models import Movie
from movie_reviewer.critics.models import Critic
import tmdbsimple as tmdb


tmdb.API_KEY = '20198fe77843ae9de92a02d9ce1e74c0'


class RecentMoviesView(View):
    template_name = 'index.html'

    def get(self, request):
        res = tmdb.Movies().popular(page=1)
        movies = res['results'][:10]
        critic = None
        if request.user.is_authenticated and not request.user.is_staff:
            critic = Critic.objects.get(id=request.user.id)
        return render(request, self.template_name, {
            'data': movies,
            'critic': critic
        })


class SearchMovieView(View):
    template_name = 'search_form.html'

    def get(self, request, *args, **kwargs):
        form = SearchForm()
        return render(request, self.template_name, {'form': form})


class SearchResults(View):
    template_name = 'search_results.html'

    def get(self, request, *args, **kwargs):
        form = SearchForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            search_dict = tmdb.Search().movie(query=data['search_input'])
            search_results = search_dict['results']
        return render(request, self.template_name, {
            'search': search_results,
            'data': data})


class MovieView(View):
    template_name = 'movie_detail.html'

    def get(self, request, id):
        get_movie = tmdb.Movies(id)
        movie_info = get_movie.info()
        db_movie = Movie.objects.filter(tmdb_id=movie_info['id']).first()
        if not db_movie:
            db_movie = Movie.objects.create(
                title=movie_info['title'],
                tmdb_id=movie_info['id'],
                overview=movie_info['overview'],
                poster_path=movie_info['poster_path'],
                release_date=movie_info['release_date']
            )
        get_credits = get_movie.credits()
        movie_credits = get_credits['cast'][:5]

        return render(request, self.template_name, {
            'movie': db_movie,
            'credits': movie_credits
        })


class MovieListView(ListView):
    model = Movie
    paginate_by = 100
    template_name = 'movie_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        return super().get_context_data(**kwargs)
