from django.core.management.base import BaseCommand
from products.models import Category, Product
from accounts.models import Accountuser

import json, os

JSON_PATH = 'products/json'

def loadFromJSON(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)

class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = loadFromJSON('categories')

        Category.objects.all().delete()
        for category in categories:
            new_category = Category(**category)
            new_category.save()

        products = loadFromJSON('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product["category"]
            _category = Category.objects.get(name=category_name)
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        super_user = Accountuser.objects.create_superuser('mrzipa', '', '21_Zipapupa', age='23',
                                                          phone='89991233443')