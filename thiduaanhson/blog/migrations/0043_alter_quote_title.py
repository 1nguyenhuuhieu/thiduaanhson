# Generated by Django 4.2 on 2023-04-17 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0042_quote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='title',
            field=models.TextField(verbose_name='trích dẫn'),
        ),
    ]