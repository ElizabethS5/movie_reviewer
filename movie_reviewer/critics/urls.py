from django.urls import path
from movie_reviewer.critics.views import (
    CreateCritic, CriticView, CriticListView)

urlpatterns = [
    path('register/', CreateCritic.as_view(), name='register'),
    path('critics/<int:pk>/', CriticView.as_view(), name='critic_detail'),
    path('critics/', CriticListView.as_view(), name='critic_list')
]
