# Generated by Django 4.2.6 on 2023-10-23 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='travelplaces',
            old_name='city',
            new_name='country',
        ),
    ]
