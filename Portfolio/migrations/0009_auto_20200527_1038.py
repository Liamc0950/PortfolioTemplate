# Generated by Django 3.0.5 on 2020-05-27 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0008_auto_20200526_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='show',
            name='title',
            field=models.CharField(default='Show Title', max_length=64),
        ),
    ]
