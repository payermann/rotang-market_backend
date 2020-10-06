from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_list),
    path('add/<int:pk>', views.add_to_cart),
    path('delete/<int:pk>', views.delete_from_cart),
    path('delete/all', views.delete_cart),
]
