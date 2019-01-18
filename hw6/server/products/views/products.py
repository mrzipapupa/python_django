from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.urls import reverse_lazy
from products.models import Product, Category
from basketapp.models import Basket
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, DetailView
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


class ProductListView(ListView):
    model = Product
    context_object_name = 'same_products'
    template_name = 'products/list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'


'''
def category_items(request, pk):
    product_list = get_list_or_404(Product.objects.filter(category_id=pk))
    title = get_object_or_404(Category, id=pk)
    content = {
        'same_products': product_list,
        'title': title
    }
    return render(request, 'products/list.html', content)
'''

''' Больше кастомизации нужно
class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'same_products'
    template_name = 'products/list.html'
'''



''' СТАРОЕ
def list_view(request, pk=None):
    title = 'Продукты'

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk:
        same_products = get_list_or_404(Product.objects.filter(Category__id=pk))
    else:
        same_products = Product.objects.all().order_by('cost')

    content = {
        'title': title,
        'same_products': same_products,
    }

    return render(request, 'products/list.html', content)
'''
'''
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
    return render(request, 'products/list.html', content)
'''

