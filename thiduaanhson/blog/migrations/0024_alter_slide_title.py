# Generated by Django 4.2 on 2023-04-12 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_slide_is_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='title',
            field=models.CharField(default='banner-<function uuid5 at 0x000002CEF97AFC70>', max_length=200, verbose_name='tiêu đề'),
        ),
    ]
