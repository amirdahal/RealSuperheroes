# Generated by Django 3.1.5 on 2021-02-09 11:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0007_auto_20210209_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('video', models.FileField(upload_to='interviews')),
                ('event_date', models.DateField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
