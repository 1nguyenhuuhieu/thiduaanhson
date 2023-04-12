# Generated by Django 4.2 on 2023-04-12 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_video_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='parrent_tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.tag', verbose_name='danh mục cha'),
        ),
        migrations.AlterField(
            model_name='video',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.author', verbose_name='tác giả'),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=200, verbose_name='tiêu đề'),
        ),
    ]