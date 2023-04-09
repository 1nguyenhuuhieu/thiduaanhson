from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import PIL.Image
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=1000, verbose_name='chuyên mục')
class Post(models.Model):
    author = models.ForeignKey('Author', verbose_name='Tác giả', blank=True, null=True, on_delete=models.CASCADE)
    is_highlight = models.BooleanField(verbose_name='có phải bài viết nổi bật', default=False)
    title = models.CharField(max_length=1000, verbose_name='Tên bài viết')
    content = RichTextUploadingField(verbose_name='nội dung')
    thumbnail = models.ImageField(upload_to='thumbnails/', verbose_name='Ảnh bìa', blank=True)
    tags = models.ManyToManyField(Tag)
    created_time = models.DateTimeField(auto_now_add=True,null=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.thumbnail:
            img = PIL.Image.open(self.thumbnail)
            width, height = img.size
            target_width = 500
            h_coefficient = width/500
            target_height = height/h_coefficient
            img = img.resize((int(target_width), int(target_height)), PIL.Image.ANTIALIAS)
            img.save(self.thumbnail.path, quality=100)
            img.close()
            self.thumbnail.close()

class Author(models.Model):
    name = models.CharField(max_length=200)
    
class Comment(models.Model):
    author = models.ForeignKey('Member', blank=True, null=True, on_delete=models.CASCADE)

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Video(models.Model):
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='cover-video/', blank=True, null=True)
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.CASCADE)
    youtube_link = models.URLField(blank=True, null=True)
    video = models.FileField(blank=True, null=True, upload_to='videos/')
    created_time = models.DateTimeField(auto_now_add=True, null=True)

