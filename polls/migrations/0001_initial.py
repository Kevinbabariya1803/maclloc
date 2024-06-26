# Generated by Django 5.0 on 2023-12-28 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/')),
                ('course_name', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='maclloc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('mobile', models.IntegerField()),
                ('email', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
    ]
