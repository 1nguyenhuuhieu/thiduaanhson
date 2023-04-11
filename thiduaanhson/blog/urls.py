
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('video/', views.video, name='video'),
    path('category/', views.category, name='category'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('category/<int:category_id>/<int:page>/', views.category, name='category'),
]
