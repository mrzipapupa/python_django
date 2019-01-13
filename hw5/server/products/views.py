from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import Http404
import json
from .models import Product, Category
from .forms import ProductForm
from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView
)

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'category', 'image', 'description', 'cost']
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:index')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'category', 'image', 'description', 'cost']
    template_name = 'products/update.html'
    success_url = reverse_lazy('products:index')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('products:index')


def products(request, pk=None):
    print(pk)

    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    if pk:
        if pk == '0':
            category = {'name': 'все'}
            products = Product.object.all().order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
        }

        return render(request, 'products/products_list.html', content)

    same_products = Product.objects.all()[3:5]

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products
    }

    return render(request, 'products/products.html', content)


# Create your views here.
def list_view(request):
    return render(
        request,
        'products/list.html',
        {
            'products': get_list_or_404(Product.objects.all())
        }
    )


def detail_view(request, pk):
    return render(
        request,
        'products/detail.html',
        {
            'object': get_object_or_404(Product, id=pk),
            'title': 'product ' + str(pk)
        }

    )
