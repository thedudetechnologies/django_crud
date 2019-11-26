from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


# from .core import views as core_views


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('core.urls')),

    # authentication urls
    path('login/', auth_views.LoginView.as_view(template_name='login.html',redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
    path('',views.home, name='index'),
    path('register/',views.signup, name='register')
]
