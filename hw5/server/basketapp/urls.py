from django.urls import path
import basketapp.views as basketapp
from django.conf.urls import url

app_name = 'basket'

urlpatterns = [
    url(r'^$', basketapp.basket, name='view'),
    url(r'^add/(?P<pk>\d+)/$', basketapp.basket_add, name='add'),
    url(r'^remove/(?P<pk>\d+)/$', basketapp.basket_remove_item, name='remove'),
    url(r'^removeall/(?P<pk>\d+)/$', basketapp.basket_remove_all, name='removeall'),
]