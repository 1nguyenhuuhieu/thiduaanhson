# Generated by Django 4.2 on 2023-04-11 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_tag_short_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='description',
            field=models.CharField(max_length=1000, null=True, verbose_name='mô tả'),
        ),
    ]
