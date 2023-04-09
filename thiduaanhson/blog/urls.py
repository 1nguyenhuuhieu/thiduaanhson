
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post, name='post'),
    path('video/', views.video, name='video'),
    path('category/', views.category, name='category'),
]
