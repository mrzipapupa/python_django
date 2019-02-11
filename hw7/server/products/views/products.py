import random
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, DetailView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from products.models import Product, Category
from basketapp.models import Basket


class ProductJsonListView(ListView):
    model = Product
    paginate_by = 2

    def serialize_object_list(self, queryset):
        return list(
            map(
                lambda itm: {
                    'id': itm.id,
                    'name': itm.name,
                    'category': itm.category.name,
                    'cost': itm.cost,
                }, queryset
            )
        )

    def get_context_data(self, **kwargs):
        context = super(ProductJsonListView, self).get_context_data(**kwargs)

        data = {}
        page = context.get('page_obj')
        route_url = reverse_lazy('rest_products:list')

        data['next_url'] = None
        data['previous_url'] = None
        data['page'] = page.number
        data['count'] = page.paginator.count
        data['result'] = self.serialize_object_list(page.object_list)

        if page.has_next():
            data['next_url'] = f'{route_url}?page={page.next_page_number}'

        if page.has_previous():
            data['previous_url'] = f'{route_url}?page={page.previous_page_number}'
        return data

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'category', 'image', 'description', 'cost']
    template_name = 'products/create.html'
    login_url = reverse_lazy('accounts:login')
    success_url = reverse_lazy('products:index')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['name', 'category', 'image', 'description', 'cost']
    template_name = 'products/update.html'
    login_url = reverse_lazy('accounts:login')
    success_url = reverse_lazy('products:index')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/delete.html'
    login_url = reverse_lazy('accounts:login')
    success_url = reverse_lazy('products:index')


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'same_products'
    template_name = 'products/list.html'
    login_url = reverse_lazy('accounts:login')
    paginate_by = 2

    '''
    def get_context_data(self, **kwargs):
        basket = get_basket(self.request.user)
        hot_product = get_hot_product()
        same_products = get_same_products(hot_product)

        return {
            'hot_product': hot_product,
            'same_products': same_products,
            'basket': basket,
        }
    '''


class ProductDetailView(UserPassesTestMixin,LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'products/detail.html'
    login_url = reverse_lazy('accounts:login')

    def test_func(self):
        return self.request.user.is_superuser


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
