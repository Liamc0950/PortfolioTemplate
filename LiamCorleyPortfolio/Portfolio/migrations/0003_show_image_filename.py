# Generated by Django 3.0.1 on 2019-12-29 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0002_auto_20191229_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='image_filename',
            field=models.CharField(default='null', max_length=256),
        ),
    ]
