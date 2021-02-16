# Generated by Django 3.1.5 on 2021-02-08 11:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0003_auto_20210208_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='updated',
        ),
        migrations.AlterField(
            model_name='news',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 8, 11, 31, 23, 95933, tzinfo=utc)),
        ),
    ]
