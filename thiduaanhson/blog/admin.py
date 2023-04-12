from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_show')
    fields = ('title', 'cover','image_tag', 'is_show','post', )
    readonly_fields = ('image_tag',)

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Member)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    

