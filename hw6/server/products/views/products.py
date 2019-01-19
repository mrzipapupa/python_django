from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.urls import reverse_lazy
from products.models import Product, Category
from basketapp.models import Basket
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, DetailView
)
import random

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


class ProductListView(ListView):
    model = Product
    context_object_name = 'same_products'
    template_name = 'products/list.html'


def products(request, pk=None):
    title = 'Продукты'
    basket = get_basket(request.user)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {
        'title': title,
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': basket,
    }
    return render(request, 'products/list.html', content)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)
    return same_products
