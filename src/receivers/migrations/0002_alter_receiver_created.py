# Generated by Django 4.2.7 on 2023-11-12 19:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receivers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiver',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 12, 20, 38, 49, 708486)),
        ),
    ]
