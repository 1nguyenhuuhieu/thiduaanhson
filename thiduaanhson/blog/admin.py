from django.contrib import admin
from .models import *
from .forms import MyModelAdminForm
# Register your models here.


class TagInline(admin.StackedInline):
    model = Tag

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_show')
    fields = ('title', 'cover','image_tag', 'is_show','post', )
    readonly_fields = ('image_tag',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    form = MyModelAdminForm
    change_form_template = 'admin/custom_ck.html'

admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Quote)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
    inlines = [TagInline, ]

    

