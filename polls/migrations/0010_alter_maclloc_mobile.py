# Generated by Django 4.2.8 on 2024-01-24 12:26

from django.db import migrations, models
import polls.models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_alter_maclloc_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maclloc',
            name='mobile',
            field=models.CharField(max_length=10, validators=[polls.models.error]),
        ),
    ]
