# Generated by Django 5.0.4 on 2024-04-11 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FactWebApp', '0005_designimages_location_designimages_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='designimages',
            name='category',
            field=models.CharField(default='Other', max_length=100),
        ),
    ]