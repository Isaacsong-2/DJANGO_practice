import datetime
from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path, include, re_path
from fcuser.views import index, logout, RegisterView, LoginView
from product.views import (
    ProductList, ProductCreate, ProductDetail,
    ProductListAPI, ProductDetailAPI
)
from order.views import OrderCreate, OrderList
from django.views.generic import TemplateView

from order.models import Order
from .functions import get_exchange
orig_index = admin.site.index


def fastcampus_index(request, extra_context=None):
    base_date = datetime.datetime.now() - datetime.timedelta(days=7)
    order_data = {}
    for i in range(7):
        target_dttm = base_date + datetime.timedelta(days=i)
        date_key = target_dttm.strftime('%Y-%m-%d')
        target_date = datetime.date(
            target_dttm.year, target_dttm.month, target_dttm.day)
        order_cnt = Order.objects.filter(
            register_date__date=target_date).count()
        order_data[date_key] = order_cnt
    extra_context = {
        'orders': order_data,
        'exchange': get_exchange(),
    }
    # return TemplateResponse(request, 'admin/index.html', extra_context)
    return orig_index(request, extra_context)


admin.site.index = fastcampus_index


urlpatterns = [
    re_path(r'^admin/manual/$', TemplateView.as_view(template_name='admin/manual.html',
                                                     extra_context={'title': '매뉴얼', 'site_title': '패스트캠퍼스', 'site_header': '패스트캠퍼스'})),
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
    path('', index),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', logout),
    path('product/', ProductList.as_view()),
    path('product/create/', ProductCreate.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()),
    path('order/create/', OrderCreate.as_view()),
    path('order/', OrderList.as_view()),

    path('api/product/', ProductListAPI.as_view()),
    path('api/product/<int:pk>', ProductDetailAPI.as_view()),
]
