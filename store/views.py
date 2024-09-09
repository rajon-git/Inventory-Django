from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView
)
from .models import *
from django_tables2.export.views import ExportMixin
import django_tables2 as tables
from .tables import ItemTable
from django_tables2 import SingleTableView

# Create your views here.

class ProductListView(ExportMixin, tables.SingleTableView):
    model = Item 
    table_class = ItemTable
    template_name = 'store/productslist.html'
    context_object_name = 'items'
    paginate_by = 10
    SingleTableView.table_pagination = False

class ProductCreateView( CreateView):
    model = Item
    template_name = 'store/productcreate.html'
    fields = ['name','category','quantity','selling_price', 'expiring_date', ]
    success_url = '/products'

    def form_valid(self, form):
        return super().form_valid(form)
    
class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    template_name = 'store/productupdate.html'
    fields = ['name','category','quantity','selling_price', 'expiring_date', 'vendor']

    def form_valid(self, form):
        return super().form_valid(form)
    
class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    template_name = 'store/productdelete.html'
    success_url = '/products'

    def test_func(self):
        item = self.get_object()