from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.apply_voucher, name='apply_voucher'),
    path('remove_voucher/', views.remove_voucher, name='remove_voucher'),

]
