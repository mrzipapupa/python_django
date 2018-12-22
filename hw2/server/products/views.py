from django.shortcuts import render
import json

# Create your views here.
def list_view(request):
    with open('data.json', 'r') as file:
        context = json.load(file)
    return render(
        request,
        'products/list.html',
        {
            'products': context.get('products') or [],
            'title': 'Products'
        }
    )


def detail_view(request, pk):
    with open('data.json', 'r') as file:
        context = json.load(file)

    products = context.get('products')

    return render(
        request,
        'products/detail.html',
        {
            'object': products[pk] if len(products) > pk else '',
            'title': 'product ' + str(pk) if len(products) > pk else ''
        }

    )