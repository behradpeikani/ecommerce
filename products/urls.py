from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.products_list, name='products_list'),
    path('<slug:slug>/', views.single_product, name='single_product'),
    path('category/<slug:slug>/', views.category_view, name='category_view'),
]
