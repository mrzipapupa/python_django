# Generated by Django 2.1.4 on 2019-01-08 11:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_auto_20181225_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
