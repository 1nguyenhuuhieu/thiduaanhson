# Generated by Django 4.2 on 2023-04-12 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_slide_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='is_show',
            field=models.BooleanField(default=True, verbose_name='hiển thị trang chủ'),
        ),
    ]