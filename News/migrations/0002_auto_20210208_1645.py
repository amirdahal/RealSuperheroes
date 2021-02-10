# Generated by Django 3.1.5 on 2021-02-08 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
