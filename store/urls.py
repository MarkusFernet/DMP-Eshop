from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_all, name='store_home'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('kategorie/<slug:category_slug>/', views.category_list, name='category_list'),
]
