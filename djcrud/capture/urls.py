from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


# from .core import views as core_views


urlpatterns = [
    path('', views.capture , name='index'),
    path('about', views.about , name='about'),
    path('services', views.services , name='services'),
    path('gallery', views.gallery , name='gallery'),
    path('blog', views.blog , name='blog'),
    path('contact', views.contact , name='contact'),
    
]
