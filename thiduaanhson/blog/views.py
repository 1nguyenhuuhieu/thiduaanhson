from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

def index(request):
    slides = Slide.objects.filter(is_show=True)[:3]
    highlight_post = Post.objects.latest('-is_highlight')
    videos = Video.objects.all().order_by('created_time')[:3]
    latest_posts = Post.objects.all().order_by('-created_time')[:5]
    context = {
        'videos': videos,
        'slides': slides,
        'highlight_post': highlight_post,
        'latest_posts': latest_posts
    }
    return render(request, 'index.html', context)

def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    try:
        post.view_count += 1
        post.save()
    except:
        pass

    context = {
        'post': post
    }
    
    return render(request, 'post.html', context)

def video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    context = {
        'video': video
    }
    return render(request, 'video.html', context)

def videos(request):
    videos = Video.objects.all()
    context = {
        'videos': videos
    }
    return render(request, 'videos.html', context)


def posts(request):
    posts = Post.objects.all().order_by('-created_time')

    context = {
        'posts': posts
    }
    return render(request, 'posts.html', context)


def category(request, category_id=None, page=1):
    if category_id:
        posts = Post.objects.filter(tags=category_id).order_by('-created_time')
    else:
        posts = Post.objects.all().order_by('-created_time')

    top_view_posts =  posts.order_by('-view_count')[:5]

    category = get_object_or_404(Tag, pk=category_id)
    objects = posts
    p = Paginator(objects, 4)
    current_page = p.page(page)
    list_object = p.page(page).object_list
    context = {
        'p': p,
        'list_object': list_object,
        'current_page': current_page,
        'category_id': category_id,
        'category': category,
        'top_view_posts': top_view_posts
    }
    return render(request, 'category.html', context)