# Generated by Django 5.2 on 2025-05-07 04:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField(default=20)),
                ('phone', models.CharField(max_length=11)),
                ('addtime', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
