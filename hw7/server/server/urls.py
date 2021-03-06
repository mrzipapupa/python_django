"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import main.views
import products.views.products
import products.views.categories

from django.conf import settings
from django.conf.urls.static import static




router = [
    path('categories/', include('products.routes.categories')),
    path('products/', include('products.routes.products')),
]

urlpatterns = [
    path('api/', include(router)),
    # path('admin/', admin.site.urls),
    path('admin/', include('adminapp.urls', namespace='admin')),
    path('products/', include('products.urls.products')),
    path('categories/', include('products.urls.categories')),
    path('accounts/', include('accounts.urls', namespace='auth')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('', include('main.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

