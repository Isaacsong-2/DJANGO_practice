from django.shortcuts import render
from django.views.generic import ListView
from .models import Order
from .forms import RegisterForm
from django.views.generic.edit import FormView
# Create your views here.


class OrderCreate(FormView):
    form_class = RegisterForm
    template_name = 'register_product.html'
    success_url = '/product/'
