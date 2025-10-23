from django.urls import path
from . import views

app_name = 'catalog_app'  # Thêm dòng này

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('product/<slug:product_slug>/', views.product_page, name='product_page'),
    path('about/', views.about, name='about'),
    path('about/company/', views.about_company, name='about_company'),
    path('about/careers/', views.careers, name='careers'),
    path('about/press/', views.press, name='press'),
    path('help/', views.help_index, name='help_index'),
    path('help/speaklife/', views.help_speaklife, name='help_speaklife'),
    path('help/sortic/', views.help_sortic, name='help_sortic'),
    path('help/vista/', views.help_vista, name='help_vista'),
    path('help/optisync/', views.help_optisync, name='help_optisync'),
    path('help/optimind/', views.help_optimind, name='help_optimind'),
    path('help/vera/', views.help_vera, name='help_vera'),
    path('help/warranty/', views.warranty_policy, name='warranty_policy'),
    path('help/purchase-guide/', views.purchase_guide, name='purchase_guide'),
    path('contact/', views.contact, name='contact'),
]
