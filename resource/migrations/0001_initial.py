# Generated by Django 2.0.5 on 2018-09-28 18:18

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('concurrency', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('concurrentmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='concurrency.ConcurrentModel')),
                ('title', models.CharField(max_length=140)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=5000)),
                ('link', models.CharField(blank=True, max_length=500, null=True, unique=True)),
                ('medium', models.CharField(max_length=150)),
                ('grade', models.CharField(max_length=150)),
                ('creator', models.CharField(max_length=150)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-creation_date',),
            },
            bases=('concurrency.concurrentmodel',),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='resources', to='resource.Tag'),
        ),
    ]
