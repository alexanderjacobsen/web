# Generated by Django 2.1.5 on 2019-01-17 22:23

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SingleFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='single_page/files/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='SingleImage',
            fields=[
                ('image', models.ImageField(upload_to='image_page/files/%Y/%m/%d')),
                ('slug', models.SlugField(primary_key=True, serialize=False, unique=True, verbose_name='url')),
            ],
        ),
        migrations.CreateModel(
            name='SinglePage',
            fields=[
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('slug', models.SlugField(primary_key=True, serialize=False, unique=True, verbose_name='url')),
            ],
        ),
        migrations.AddField(
            model_name='singlefile',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='single_page.SinglePage'),
        ),
    ]
