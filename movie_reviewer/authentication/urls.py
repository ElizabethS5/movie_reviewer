from django.urls import path
from movie_reviewer.authentication.views import (login_view, logout_view)

urlpatterns = [

    # Functions
    path('login/', login_view, name="login"),
    path('log_out/', logout_view, name="log_out"),

]
