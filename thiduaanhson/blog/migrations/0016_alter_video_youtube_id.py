# Generated by Django 4.2 on 2023-04-12 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_tag_parrent_tag_alter_video_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='youtube_id',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='id video youtube'),
        ),
    ]
