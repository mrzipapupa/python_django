# Generated by Django 2.1.4 on 2018-12-25 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_accountuser_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
