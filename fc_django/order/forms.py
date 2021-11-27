from django import forms
from .models import Order
from django.contrib.auth.hashers import check_password, make_password


class RegisterForm(forms.Form):
    quantity = forms.IntegerField(
        error_messages={
            'required': '수량량을 입력해주세요'
        },
        label='수량'
    )
    product = forms.IntegerField(
        error_messages={
            'required': '상품을 입력해주세요'
        },
        label='상품', widget=forms.HiddenInput
    )

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
