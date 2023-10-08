from django.core.cache import cache
from django.contrib.auth import get_user_model
from rest_framework_mongoengine.generics import ListAPIView

from api.serializers.product_serializers import (
    CategorySerializer,
    ProductSerializer,
    ProductBookmarkSerializer,
    OrderSerializer,
)
from products.models import User
from products import logic as product_logic
from orders import logic as order_logic


AuthUser = get_user_model()


def get_mongo_user(auth_user: AuthUser):
    if user := cache.get(auth_user) is None:
        user = User.objects(username=user.username)
        cache.set("user", user)
    return user


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return product_logic.get_category_q()


class ProductsListView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        products_q = product_logic.get_products_q()
        return products_q


class ProductBookmarkListView(ListAPIView):
    serializer_class = ProductBookmarkSerializer

    def get_queryset(self):
        return product_logic.get_user_bookmarks_q(
            get_mongo_user(auth_user=self.request.user)
        )


class OrderListView(ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        order_logic.get_user_orders_q(get_mongo_user(auth_user=self.request.user))
