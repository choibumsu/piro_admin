from django.urls import path
from . import views

app_name = "items"

urlpatterns = [
    path("", views.main, name="main"),

    path("item/detail/<int:pk>", views.item_detail, name="item_detail"),
    path("item/create/", views.item_create, name="item_create"),
    path("item/update/<int:pk>", views.item_update, name="item_update"),
    path("item/delete/<int:pk>", views.item_delete, name="item_delete"),
    path("item/decrease/amount/<int:pk>",
         views.item_decrease, name="item_decrease"),
    path("item/increase/amount/<int:pk>",
         views.item_increase, name="item_increase"),

    path("customer/list/", views.customer_list, name="customer_list"),
    path("customer/detail/<int:pk>", views.customer_detail, name="customer_detail"),
    path("customer/create/", views.customer_create, name="customer_create"),
    path("customer/update/<int:pk>", views.customer_update, name="customer_update"),
    path("customer/delete/<int:pk>", views.customer_delete, name="customer_delete"),
]
