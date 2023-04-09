from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html', context={})

def post(request):
    post = Post.objects.get(pk=2)

    context = {
        'post': post
    }
    
    return render(request, 'post.html', context)

def video(request):
    return render(request, 'video.html', context={})

def category(request):
    return render(request, 'category.html', context={})