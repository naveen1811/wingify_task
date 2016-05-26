from rest_framework import serializers

from store.models import Products


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        exclude = ['is_active', 'store_id']