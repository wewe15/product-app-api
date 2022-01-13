from django.urls import path
from .views import ProductListView, ProductDetailView


urlpatterns = [
    path('<uuid:pk>', ProductDetailView.as_view(),
         name='product-detail'),
    path('', ProductListView.as_view(), name='product-list'),
]
