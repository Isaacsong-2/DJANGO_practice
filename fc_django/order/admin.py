from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.contrib import admin
from .models import Order
from django.db import transaction
from django.utils.html import format_html
# Register your models here.


def refund(modeladmin, request, queryset):
    with transaction.atomic():
        qs = queryset.filter(~Q(status='환불'))

        ct = ContentType.objects.get_for_model(queryset.model)

        for obj in qs:
            obj.product.stock += obj.quantity
            obj.product.save()

            LogEntry.objects.log_action(
                user_id=request.user.id,
                content_type_id=ct.pk,
                object_id=obj.pk,
                object_repr='주문 환불',
                action_flag=CHANGE,
                change_message='주문 환불'
            )
        qs.update(status='환불')


refund.short_description = '환불'


class OrderAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('fcuser', 'product', 'styled_status')

    actions = [
        refund
    ]

    def refund(self, request, queryset):
        pass

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': '주문 목록'}
        return super().changelist_view(request, extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        order = Order.objects.get(pk=object_id)
        extra_context = {
            'title': f"'{order.fcuser.email}'의 '{order.product}' 주문 수정하기"}
        return super().changeform_view(request, object_id, form_url, extra_context)

    def styled_status(self, obj):
        if obj.status == '환불':
            # obj.status
            return format_html(f'<span style="color:red">{obj.status}</span>')
        if obj.status == '결제완료':
            # obj.status
            return format_html(f'<span style="color:green">{obj.status}</span>')
        return format_html(f'<b>{obj.status}</b>')

    styled_status.short_description = '상태'


admin.site.register(Order, OrderAdmin)
