from django.urls import path

from product import views

urlpatterns = [
    path("<int:id>/", views.ProductDetails.as_view(), name="product_details"),
    path('', views.ProductList.as_view(), name="product_list"),
]