
from django.contrib import admin
from django.urls import path, include
from fcuser.views import index, logout, RegisterView, LoginView
from product.views import (
    ProductList, ProductCreate, ProductDetail,
    ProductListAPI, ProductDetailAPI
)
from order.views import OrderCreate, OrderList
urlpatterns = [
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
