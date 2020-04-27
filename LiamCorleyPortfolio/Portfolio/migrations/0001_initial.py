# Generated by Django 3.0.5 on 2020-04-27 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(default='Null', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('detail_text', models.CharField(max_length=512)),
                ('sort_order', models.IntegerField()),
                ('cover_image', models.ImageField(default='default.png', upload_to='')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portfolio.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=200)),
                ('image_filename', models.CharField(max_length=256)),
                ('sort_order', models.IntegerField()),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portfolio.Show')),
            ],
        ),
    ]