# from django.contrib import admin
from django.urls import path

from bazaar.views import product_detail
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('bazaar/<int:product_id>/', product_detail, name='product_detail'),

]
