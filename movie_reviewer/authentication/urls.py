from django.urls import path
from movie_reviewer.authentication.views import *

urlpatterns = [

    # Functions
    path('login/', login_view, name="login"),
    path('log_out/', logout_view, name="log_out"),
  
]