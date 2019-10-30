from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('products/list/', views.product_list, name='products-list'),
    path('products/<int:pk>/', views.product_detail, name='products-detail')
]