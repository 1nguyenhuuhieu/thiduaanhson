from django import forms
from .models import Post

class MyModelAdminForm(forms.ModelForm):
    class Media:
        js = ('js/init_ckeditor.js',)  # Path to your custom JS file

    class Meta:
        model = Post
        fields = '__all__'
