# Generated by Django 4.2 on 2023-04-17 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0037_alter_post_youtube_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.IntegerField(choices=[(0, 'VĂN BẢN'), (1, 'THI ĐUA'), (2, 'KHEN THƯỞNG')], default=1),
            preserve_default=False,
        ),
    ]
