# Generated by Django 2.0.5 on 2018-09-29 15:42

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('concurrency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentBox',
            fields=[
                ('concurrentmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='concurrency.ConcurrentModel')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
            bases=('concurrency.concurrentmodel',),
        ),
    ]
