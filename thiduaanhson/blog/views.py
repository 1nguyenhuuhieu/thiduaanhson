from django.shortcuts import render
from .models import *
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
        highlight_post = Post.objects.latest('-is_highlight', '-updated_time')
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