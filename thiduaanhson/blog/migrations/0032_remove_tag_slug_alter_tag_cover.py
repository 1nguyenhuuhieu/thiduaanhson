# Generated by Django 4.2 on 2023-04-13 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_remove_post_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='slug',
        ),
        migrations.AlterField(
            model_name='tag',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='cover-tag/', verbose_name='ảnh bìa'),
        ),
    ]
