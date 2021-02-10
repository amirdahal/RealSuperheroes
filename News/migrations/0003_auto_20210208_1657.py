# Generated by Django 3.1.5 on 2021-02-08 11:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_auto_20210208_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='updated_at',
            new_name='updated',
        ),
        migrations.AlterField(
            model_name='news',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
