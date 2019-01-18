from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, get_list_or_404
from basketapp.models import Basket
from products.models import Product


def basket(request):
    counter, cost = 0, 0
    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if basket:
        counter = get_counter_basket()
        cost = get_cost_basket()

    content = {
        'basket': basket,
        'count': counter,
        'cost': cost
    }

    return render(request, 'basketapp/basket.html', content)


def basket_add(request, pk):
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


def basket_remove_all(request):
    items = get_list_or_404(Basket.objects.all(user=request.user))
    for itm in items:
        itm.delete()
        itm.save()


def get_cost_basket():
    cost = 0
    products = get_list_or_404(Basket.objects.all())
    for itm in products:
        cost += itm.quantity * itm.product.cost
    return cost


def get_counter_basket():
    counter = 0
    products = get_list_or_404(Basket.objects.all())
    for itm in products:
        counter += itm.quantity
    return counter