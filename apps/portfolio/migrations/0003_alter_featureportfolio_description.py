# Generated by Django 5.1.3 on 2024-12-03 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_featureportfolio_galleryportfolio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featureportfolio',
            name='description',
            field=models.TextField(max_length=255),
        ),
    ]
