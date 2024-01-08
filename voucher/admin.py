from django.contrib import admin

# Register your models here.

from .models import Voucher

@admin.register(Voucher)
class VoucherAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_percentage', 'active')
    list_filter = ('active',)
    search_fields = ('code',)