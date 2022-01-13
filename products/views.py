from rest_framework import generics
from .models import Product
from .permissions import IsAuthorOrReadOnly
from .serializers import ProductSerializer


class ProductListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(seller=user).order_by("price")


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = ProductSerializer
    queryset = Product.objects.order_by("price")
