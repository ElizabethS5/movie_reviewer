# from django.urls import path

from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # Functions
    path('login/', views.login_user, name="login"),
    path('sign_out/', views.sign_out, name="sign_out"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)