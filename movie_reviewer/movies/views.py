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
import re
from django.shortcuts import render
from django.views import View
from movie_reviewer.movies.forms import SearchForm
# from movie_reviewer.movies.models import Movie
import tmdbsimple as tmdb 


tmdb.API_KEY = '20198fe77843ae9de92a02d9ce1e74c0'

class RecentMoviesView(View):
    template_name = 'index.html'

    def get(self, request):
        res = tmdb.Movies().popular(page=1)
        movies= res['results'][:10]
        return render(request, self.template_name, {'data': movies})

class SearchMovieView(View):
    template_name = 'search_form.html'

    def get(self, request, *args, **kwargs):
        form = SearchForm()
        return render(request, self.template_name, {'form': form})

class SearchResults(View):
    template_name = 'search.html'
    
    def get(self, request, *args, **kwargs):
        form = SearchForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            search_dict = tmdb.Search().movie(query=data['search_input'])
            search_results = search_dict['results']
        return render(request, self.template_name, {'search': search_results})

class MovieView(View):
    template_name = 'movie_detail.html'

    def get(self, request, id):
        get_movie = tmdb.Movies(id)
        movie = get_movie.info()
        get_credits = get_movie.credits()
        movie_credits = get_credits['cast'][:5]
        return render(request, self.template_name, {'movie': movie, 'credits': movie_credits})