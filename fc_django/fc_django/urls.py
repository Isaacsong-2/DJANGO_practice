
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

orig_index = admin.site.index


def fastcampus_index(request, extra_context=None):
    extra_context = {'test': 'test'}
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
