from django.urls import path
from django.conf.urls import url
from products.views.categories import CategoryListView, CategoryCreateView,\
    CategoryUpdateView, CategoryDeleteView, CategoryDetailView

app_name="categories"



urlpatterns = [
    path('', CategoryListView.as_view(), name='category'),
    path('create/', CategoryCreateView.as_view(), name='create'),
    path('<int:pk>/update/', CategoryUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', CategoryDeleteView.as_view(), name='delete'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='detail'),
]