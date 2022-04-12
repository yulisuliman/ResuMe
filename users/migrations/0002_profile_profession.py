# Generated by Django 4.0.3 on 2022-04-01 20:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profession',
            field=models.TextField(blank=True,
                                   max_length=100,
                                   validators=[django.core.validators.MaxLengthValidator(100)]),
        ),
    ]