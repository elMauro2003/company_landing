# Generated by Django 5.1.3 on 2025-02-19 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0029_contactsection_portfoliosection_pricingsection_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_section_one', models.CharField(max_length=50)),
                ('title_section_two', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
