# Generated by Django 2.2.4 on 2020-01-14 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uptake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('button_link', models.TextField()),
                ('text', models.TextField()),
                ('published', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['published'],
            },
        ),
    ]
