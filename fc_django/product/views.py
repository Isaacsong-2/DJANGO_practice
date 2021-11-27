from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from django.views.generic.edit import FormView
from .forms import RegisterForm
from order.forms import RegisterForm as OrderForm
# Create your views here.


class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'


class ProductCreate(FormView):
    form_class = RegisterForm
    template_name = 'register_product.html'
    success_url = '/product/'


class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm(self.request)
        return context
