from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('sign_in/', views.sign_in_view, name='sign_in'),
    path('sign_up/', views.sign_up_view, name='sign_up'),
    path('sign_out/', views.sign_out_view, name='sign_out'),
    path("add_address/", views.add_address, name="add_address"),
]
