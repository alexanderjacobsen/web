# Generated by Django 2.0.5 on 2018-07-30 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0008_auto_20180716_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='projects',
        ),
    ]
