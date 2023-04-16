
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('posts/', views.tag, name='posts'),
    path('tag/<int:tag_id>/', views.tag, name='tag'),
    path('tag/<int:tag_id>/<int:page>/', views.tag, name='tag_paginate'),
]
