# Generated by Django 3.0.5 on 2020-04-27 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0002_auto_20200427_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='cd',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='show',
            name='dir',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='show',
            name='ld',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='show',
            name='photo',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='show',
            name='projd',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='show',
            name='props',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='show',
            name='sd',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='show',
            name='sm',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
