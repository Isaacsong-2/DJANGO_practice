from django.shortcuts import render, redirect
from django.views.generic import ListView

# from fc_django.fcuser.decorators import login_required
from .models import Order
from .forms import RegisterForm
from fcuser.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from django.db import transaction
from product.models import Product
from fcuser.models import Fcuser
# Create your views here.


@method_decorator(login_required, name='dispatch')
class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):
        with transaction.atomic():
            prod = Product.objects.get(pk=form.data.get('product'))
            order = Order(
                quantity=int(form.data.get('quantity')),
                product=prod,
                fcuser=Fcuser.objects.get(
                    email=self.request.session.get('user'))
            )
            order.save()
            prod.stock -= int(form.data.get('quantity'))
            prod.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return redirect('/product/' + str(form.data.get('product')))

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw


@ method_decorator(login_required, name='dispatch')
class OrderList(ListView):
    template_name = 'order.html'
    context_object_name = 'order_list'

    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(
            fcuser__email=self.request.session.get('user'))
        return queryset
