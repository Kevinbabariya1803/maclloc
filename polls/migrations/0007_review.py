# Generated by Django 4.2.8 on 2024-01-05 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_courses_content2_courses_content_head2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/')),
                ('name', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]