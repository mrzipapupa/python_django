# Generated by Django 2.1.4 on 2018-12-23 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20181221_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]
