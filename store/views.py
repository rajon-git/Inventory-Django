from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
)
from .models import *

# Create your views here.
class ProductCreateView( CreateView):
    model = Item
    template_name = 'store/productcreate.html'
    fields = ['name','category','quantity','selling_price', 'expiring_date', ]
    success_url = '/products'

    def form_valid(self, form):
        return super().form_valid(form)