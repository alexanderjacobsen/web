# Generated by Django 2.1.5 on 2019-01-13 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='web/img/projects/'),
        ),
    ]
