# Generated by Django 4.2 on 2023-04-12 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_slide'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='bài viết liên kết'),
        ),
    ]
