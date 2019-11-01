from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.photo_list, name='photo_list'),
]