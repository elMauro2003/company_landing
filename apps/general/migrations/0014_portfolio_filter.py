# Generated by Django 5.1.3 on 2024-12-02 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0013_alter_services_color_alter_services_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='filter',
            field=models.CharField(default='app', max_length=100),
        ),
    ]