# Generated by Django 2.2.26 on 2022-02-01 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20220201_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='likes',
        ),
        migrations.AddField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
