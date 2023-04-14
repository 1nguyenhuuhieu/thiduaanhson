
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('videos/', views.videos, name='videos'),
    path('video/<int:video_id>/', views.video, name='video'),
    path('posts/', views.posts, name='posts'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('category/<int:category_id>/<int:page>/', views.category, name='category'),
]
