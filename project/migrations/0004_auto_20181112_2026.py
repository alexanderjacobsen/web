# Generated by Django 2.0.5 on 2018-11-12 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20181112_1957'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicantpool',
            old_name='application_end',
            new_name='application_end_date',
        ),
    ]
