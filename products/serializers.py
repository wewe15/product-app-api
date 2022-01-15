from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    seller = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = Product
        fields = ('id', 'name', 'seller', 'price')
