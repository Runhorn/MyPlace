# Generated by Django 3.0.6 on 2020-10-12 08:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_and_surname', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=10)),
                ('photo', models.ImageField(upload_to='media/%Y/%m/%d')),
                ('email', models.CharField(max_length=30)),
                ('joined', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
