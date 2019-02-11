from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from accounts.models import Accountuser
from products.models import Product
from products.models import Category
from accounts.forms import RegisterForm, EditForm
from products.forms.categories import CategoryForm
from adminapp.forms import ShopUserAdminEditForm
from adminapp.forms import ProductCategoryEditForm

@user_passes_test(lambda u: u.is_superuser)
def users (request):
    title = 'админка/пользователи'
    users_list = Accountuser.objects.all().order_by( '-is_active' , '-is_superuser' , '-is_staff' , 'username' )
    content = {
        'title' : title,
        'objects' : users_list
    }
    return render(request, 'adminapp/users.html' , content)


def user_create(request):
    title = 'пользователи/создание'

    if request.method == 'POST':
        user_form = RegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse_lazy('admin:users'))
    else:
        user_form = RegisterForm()

    content = {'title': title, 'update_form': user_form}

    return render(request, 'adminapp/user_update.html', content)


def user_update (request, pk):
    title = 'пользователи/редактирование'

    edit_user = get_object_or_404(Accountuser, pk=pk)
    if request.method == 'POST':
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse_lazy('admin:user_update', args={edit_user.pk}))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)

    content = {'title': title, 'update_form': edit_form}

    return render(request, 'adminapp/user_update.html', content)


def user_delete (request, pk):
    title = 'пользователи/удаление'

    user = get_object_or_404(Accountuser, pk=pk)

    if request.method == 'POST':
        user.delete()
        # user.is_active = False
        # user.save()
        return HttpResponseRedirect(reverse_lazy('admin:users'))

    content = {'title': title, 'user_to_delete': user}

    return render(request, 'adminapp/user_delete.html', content)


def categories(request):
    title = 'админка/категории'

    categories_list = Category.objects.all()

    content = {
        'title': title,
        'objects': categories_list
    }
    return render(request, 'adminapp/category.html', content)


def category_create (request):
    title = 'категории/создание'

    if request.method == 'POST':
        user_form = CategoryForm(request.POST, request.FILES) # RegisterForm????
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse_lazy('admin:categories'))
    else:
        user_form = CategoryForm()

    content = {'title': title, 'update_form': user_form}

    return render(request, 'adminapp/category_update.html', content)

def category_update(request, pk):
    title = 'категории/редактирование'

    edit_category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse_lazy('admin:category_update', args={edit_category.pk}))
    else:
        edit_form = ProductCategoryEditForm(instance=edit_category)

    content = {'title': title, 'update_form': edit_form}

    return render(request, 'adminapp/category_update.html', content)

def category_delete(request, pk):
    title = 'категории/удаление'

    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        category.delete()
        # user.is_active = False
        # user.save()
        return HttpResponseRedirect(reverse_lazy('admin:categories'))

    content = {'title': title, 'category_to_delete': category}

    return render(request, 'adminapp/category_delete.html', content)

def products(request, pk):
    title = 'админка/продукт'

    category = get_object_or_404(Category, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')
    content = {
        'title': title,
        'category': category,
        'objects': products_list,
    }
    return render(request, 'adminapp/products.html', content)

def product_create(request, pk):
    pass

def product_read(request, pk):
    pass

def product_update(request, pk):
    pass

def product_delete(request, pk):
    pass