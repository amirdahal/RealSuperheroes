# Generated by Django 3.1.5 on 2021-02-09 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0006_auto_20210209_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.category'),
        ),
    ]
