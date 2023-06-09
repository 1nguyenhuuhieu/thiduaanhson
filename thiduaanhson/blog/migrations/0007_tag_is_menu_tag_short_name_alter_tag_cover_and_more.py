# Generated by Django 4.2 on 2023-04-11 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_tag_cover_tag_parrent_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='is_menu',
            field=models.BooleanField(default=False, verbose_name='hiển thị trên menu'),
        ),
        migrations.AddField(
            model_name='tag',
            name='short_name',
            field=models.CharField(default=1, max_length=20, verbose_name='tên hiển thị ở menu'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tag',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='cover-category/', verbose_name='ảnh bìa'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='parrent_tag',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.tag', verbose_name='danh mục cha'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=1000, verbose_name='tên đầy đủ'),
        ),
    ]
