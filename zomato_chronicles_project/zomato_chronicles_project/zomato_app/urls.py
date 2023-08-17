from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dishes/', views.dish_list, name='dish_list'),
    path('add/', views.add_dish, name='add_dish'),
    path('orders/', views.order_list, name='order_list'),
    path('place_order/', views.place_order, name='place_order'),
]
