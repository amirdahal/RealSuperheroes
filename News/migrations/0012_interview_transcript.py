# Generated by Django 3.1.6 on 2021-02-17 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0011_interview_subtitles'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='transcript',
            field=models.TextField(default='Data unavailable!'),
        ),
    ]
