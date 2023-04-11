from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
import re
# as per recommendation from @freylis, compile once only
CLEANR = re.compile('<.*?>') 

# Create your views here.
def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

def index(request):

    # get latest highlight post
    try:
        highlight_post = Post.objects.latest('is_highlight', 'updated_time')
        plaintext_post = cleanhtml(highlight_post.content)
    except:
        highlight_post = None
        plaintext_post = None

    videos = Video.objects.all()
    context = {
        'highlight_post': highlight_post,
        'videos': videos,
        'plaintext_post': plaintext_post
    }
    return render(request, 'index.html', context)

def post(request, post_id):
    post = Post.objects.get(pk=post_id)

    context = {
        'post': post
    }
    
    return render(request, 'post.html', context)

def video(request):
    return render(request, 'video.html', context={})

def category(request, category_id=None, page=1 ):
    if category_id:
        posts = Post.objects.filter(category=category_id).order_by('-created_time')
    else:
        posts = Post.objects.all().order_by('-created_time')

    objects = posts
    p = Paginator(objects, 2)
    current_page = p.page(page)
    list_object = p.page(page).object_list
    context = {
        'p': p,
        'list_object': list_object,
        'current_page': current_page,
        'category_id': category_id
    }
    return render(request, 'category.html', context)