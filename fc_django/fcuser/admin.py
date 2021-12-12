from django.contrib import admin
from .models import Fcuser
# Register your models here.


class FcuserAdmin(admin.ModelAdmin):
    list_display = ('email',)

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': '사용자 목록'}
        return super().changelist_view(request, extra_context)


admin.site.register(Fcuser, FcuserAdmin)
