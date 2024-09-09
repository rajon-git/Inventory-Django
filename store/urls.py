from django.contrib import admin
from django.urls import path
from .views import (
    ProductCreateView,
)

urlpatterns = [
    path('new-product/', ProductCreateView.as_view(), name='product-create'),
]
