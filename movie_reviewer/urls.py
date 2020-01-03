"""movie_reviewer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movie_reviewer.authentication.urls import urlpatterns as auth_urls
from movie_reviewer.critics.urls import urlpatterns as critic_urls
from movie_reviewer.movies.urls import urlpatterns as movie_urls
from movie_reviewer.reviews.urls import urlpatterns as review_urls

from movie_reviewer.critics.models import Critic
from movie_reviewer.movies.models import Movie
from movie_reviewer.reviews.models import Review

# All models are registered with the admin interface
admin.site.register(Critic)
admin.site.register(Movie)
admin.site.register(Review)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += auth_urls

urlpatterns += critic_urls

urlpatterns += movie_urls

urlpatterns += review_urls
