# Generated by Django 5.1.3 on 2024-12-03 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_featureportfolio_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='featureportfolio',
            name='icon',
            field=models.CharField(default='bi bi-1-square-fill', max_length=80),
        ),
    ]
