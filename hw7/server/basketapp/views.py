from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from basketapp.models import Basket
from products.models import Product

@login_required
def basket(request):
    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    content = {
        'basket': basket,
    }

    return render(request, 'basketapp/basket.html', content)


@login_required
def basket_add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        print('2')
        return HttpResponseRedirect(reverse('products:index', args=[pk]))
    product = get_object_or_404(Product, pk=pk)
    old_basket_item = Basket.objects.filter(user=request.user, product=product)

    if old_basket_item:
        old_basket_item[0].quantity += 1
        old_basket_item[0].save()
    else:
        new_basket_item = Basket(user=request.user, product=product)
        new_basket_item.quantity += 1
        new_basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove_item(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket_item = Basket.objects.get(user=request.user, product=product)
    if basket_item.quantity > 0:
        basket_item.quantity -= 1
        basket_item.save()
    elif basket_item.quantity == 0:
        basket_item.delete()
        basket_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove_all(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


