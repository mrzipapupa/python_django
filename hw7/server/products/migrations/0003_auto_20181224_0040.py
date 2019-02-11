# Generated by Django 2.1.4 on 2018-12-23 14:40

from django.db import migrations
import json

def create_categories(apps, schema_editor):
    model_class = apps.get_model('products.category')
    with open('products/Fixtures/categories.json', 'r') as file:
        for date in json.load(file):
            model_class.objects.create(
                name = date.get("name")
            )

class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20181224_0030'),
    ]

    operations = [
        migrations.RunPython(
            create_categories,
            lambda x,y: (x,y)
        )
    ]
