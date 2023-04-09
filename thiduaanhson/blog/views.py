from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    videos = Video.objects.all()
    context = {
        'videos': videos
    }
    return render(request, 'index.html', context)

def post(request):
    post = Post.objects.get(pk=1)


    context = {
        'post': post
    }
    
    return render(request, 'post.html', context)

def video(request):
    return render(request, 'video.html', context={})

def category(request):
    return render(request, 'category.html', context={})