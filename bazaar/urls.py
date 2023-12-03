from django.urls import path
from . import views

urlpatterns = [
    path('', views.bazaar, name='bazaar'),
    path('<product_id>', views.product_detail, name='product_detail'),

]
