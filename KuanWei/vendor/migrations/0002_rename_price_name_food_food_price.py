# Generated by Django 4.1.4 on 2023-01-12 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='price_name',
            new_name='food_price',
        ),
    ]
