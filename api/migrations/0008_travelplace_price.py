# Generated by Django 5.0.1 on 2024-03-08 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_ticket_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelplace',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]