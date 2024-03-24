from django.urls import path
from . import views

urlpatterns = [
    path("product/create", views.create_product_view, name="create_product_view"),
    path(
        "products/<int:product_id>",
        views.retrieve_product_view,
        name="retrieve_product_view",
    ),
]
