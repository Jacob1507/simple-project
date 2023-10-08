from rest_framework_mongoengine import serializers

from products.models import Category, Product, ProductBookmark
from orders.models import OrderDetail, Order


class CategorySerializer(serializers.DocumentSerializer):
    class Meta:
        model = Category


class ProductSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Product


class ProductBookmarkSerializer(serializers.DocumentSerializer):
    class Meta:
        model = ProductBookmark


class OrderDetailSerializer(serializers.DocumentSerializer):
    class Meta:
        model = OrderDetail


class OrderSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Order
