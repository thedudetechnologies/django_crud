from django.contrib import admin
from django.urls import path 
from django.contrib import auth
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url, include


# from .core import views as core_views


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('core.urls')),

    # authentication urls
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', auth_views.logout, name='logout'),
    path('',views.home, name='home'),
    path('register/',views.signup, name='register')
]
