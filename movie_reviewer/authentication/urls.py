from django.urls import path
from movie_reviewer.authentication.views import *

urlpatterns = [

    # Functions
    path('login/', login, name="login"),
    path('log_out/', log_out, name="log_out"),
   
]