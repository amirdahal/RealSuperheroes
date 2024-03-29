# Generated by Django 3.1.5 on 2021-02-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=100)),
                ('Subject', models.CharField(max_length=30)),
                ('Message', models.TextField()),
                ('Read', models.BooleanField(default=False)),
            ],
        ),
    ]
