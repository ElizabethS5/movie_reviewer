from django.urls import path
from django.contrib import admin
from movie_reviewer.reviews import views

urlpatterns = [
path('admin/', admin.site.urls),
path('', views.index, name='homepage'),

path('review/', views.review_view),
path('reviewadd/', views.reviewaddview),



 ]

