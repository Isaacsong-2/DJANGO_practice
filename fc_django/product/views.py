from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
from django.views.generic.edit import FormView
from .forms import RegisterForm
# Create your views here.


class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'


class ProductCreate(FormView):
    form_class = RegisterForm
    template_name = 'register_product.html'
    success_url = '/product/'
