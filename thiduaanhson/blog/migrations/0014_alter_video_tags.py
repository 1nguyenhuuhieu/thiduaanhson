# Generated by Django 4.2 on 2023-04-12 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_video_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='tags',
            field=models.ManyToManyField(to='blog.tag', verbose_name='danh mục'),
        ),
    ]
