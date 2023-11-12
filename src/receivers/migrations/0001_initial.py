# Generated by Django 4.2.7 on 2023-11-12 19:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('website', models.URLField(blank=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2023, 11, 12, 20, 22, 27, 521970))),
            ],
        ),
    ]
