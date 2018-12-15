from django.shortcuts import render

# Create your views here.

def main_view(request):
    return render(request, 'main/index.html')


def contacts_view(request):
    return render(request, 'main/contacts.html')


def about_view(request):
    return render(request, 'main/about.html')
