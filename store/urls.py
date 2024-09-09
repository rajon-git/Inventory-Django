from django.contrib import admin
from django.urls import path
from .views import (
    ProductListView,
    ProductCreateView,
)

urlpatterns = [
    path('products/',ProductListView.as_view(), name="productslist"),
    path('new-product/', ProductCreateView.as_view(), name='product-create'),
]
