# Generated by Django 4.2 on 2023-04-16 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0035_remove_member_user_remove_video_author_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'bình luận', 'verbose_name_plural': 'bình luận'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='youtube_id',
        ),
        migrations.AddField(
            model_name='post',
            name='is_public',
            field=models.BooleanField(default=True, verbose_name='có hiển thị bài viết'),
        ),
        migrations.AddField(
            model_name='post',
            name='youtube_url',
            field=models.URLField(blank=True, help_text='copy url video youtube vào đây', max_length=20, null=True, verbose_name='id video youtube'),
        ),
    ]
