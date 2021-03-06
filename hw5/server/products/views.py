from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Product, Category
from basketapp.models import Basket
from django.views.generic import (
    CreateView, UpdateView, DeleteView
)
from basketapp.views import get_cost_basket, get_counter_basket

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


def list_view(request, pk=None):
    title = 'Продукты'
    basket = []
    cost = 0
    counter = 0

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if basket:
        counter = get_counter_basket()
        cost = get_cost_basket()

    if pk:
        same_products = get_list_or_404(Product.objects.filter(Category__id=pk))
    else:
        same_products = Product.objects.all().order_by('cost')

    content = {
        'title': title,
        'same_products': same_products,
        'basket': basket,
        'count': counter,
        'cost': cost,
    }

    return render(request, 'products/list.html', content)


def detail_view(request, pk):
    return render(
        request,
        'products/detail.html',
        {
            'object': get_object_or_404(Product, id=pk),
            'title': 'product ' + str(pk)
        }
    )

def category_view(request):
    categories = get_list_or_404(Category)
    content = {'category': categories }
    return render(request, 'products/category_list.html', content)


def category_items(request, pk):
    product_list = get_list_or_404(Product.objects.filter(category_id=pk))
    title = get_object_or_404(Category, id=pk)
    content = {
        'same_products': product_list,
        'title': title
    }
    return render(request, 'products/list.html', content)