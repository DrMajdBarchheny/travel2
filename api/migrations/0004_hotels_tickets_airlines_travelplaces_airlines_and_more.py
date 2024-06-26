# Generated by Django 4.2.6 on 2023-10-23 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_touristsites_travelplaces_toursites'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('H_photo', models.ImageField(blank=True, null=True, upload_to='hotels_ph')),
                ('rate', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AirLines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='airlines_ph')),
                ('tickets', models.ManyToManyField(to='api.tickets')),
            ],
        ),
        migrations.AddField(
            model_name='travelplaces',
            name='airlines',
            field=models.ManyToManyField(to='api.airlines'),
        ),
        migrations.AddField(
            model_name='travelplaces',
            name='hotels',
            field=models.ManyToManyField(to='api.hotels'),
        ),
    ]
