# Generated by Django 5.0 on 2023-12-28 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='view_more',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
