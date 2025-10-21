from django.urls import path
from . import views

app_name = 'catalog_app'  # Thêm dòng này

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('product-detail/', views.product_detail, name='product_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
