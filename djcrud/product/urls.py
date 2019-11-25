from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


# from .core import views as core_views


urlpatterns = [
    path('category/',views.add_category , name='categories'),
    path('category/edit/<int:id>/', views.edit_cat, name='edits'),
    path('category/delete/<int:id>/', views.destroy_cat, name='deletes'),
    path('product/',views.add_product , name='add_product'),
    path('show/', views.show_product, name='crud_product'),
    path('edit/<int:id>/', views.edit_product, name='edit_product'),
    path('delete/<int:id>/', views.destroy_product, name='delete_product'),

]