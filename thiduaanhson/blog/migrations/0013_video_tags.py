# Generated by Django 4.2 on 2023-04-12 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_video_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.tag', verbose_name='danh mục'),
        ),
    ]
