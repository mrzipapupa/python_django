from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from django.urls import reverse_lazy
from django.http import JsonResponse

from products.models import Category


class CategoryJsonListView(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        query = self.model.objects.all()

        return {
            'results': list(
                map (
                    lambda itm: {
                        'id': itm.id,
                        'name': itm.name,
                        # 'created': itm.created,
                        # 'modified': itm.modified,
                    },
                    query
                )
            )
        }

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)

class CategoryListView(ListView):
    model = Category
    context_object_name = 'category'
    template_name = 'categories/list.html'


class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'categories/detail.html'

    def get_context_data(self, **kwargs):
        obj = kwargs.get('object')
        products = obj.product_set.all()

        return {
            'object': obj,
            'products': products
        }


class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'categories/create.html'
    success_url = reverse_lazy('categories:category')


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'categories/update.html'
    success_url = reverse_lazy('categories:category')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'categories/delete.html'
    success_url = reverse_lazy('categories:category')


