from rest_framework import generics
from .models import Product
from .permissions import IsAuthorOrReadOnly
from .serializers import ProductSerializer


class ProductListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all().order_by('price')
        sellers = self.request.query_params.get('seller')

        if sellers:
            queryset = queryset.filter(seller_id=sellers).order_by('price')

        return queryset


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = ProductSerializer
    queryset = Product.objects.order_by("price")
