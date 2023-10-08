from django.db.models import QuerySet
from django.contrib.auth import get_user_model

from products.models import Product, ProductBookmark, Order


User = get_user_model()


def get_products_q(category_slug: str) -> QuerySet[Product]:
    """Returns products by category"""
    products_by_category = Product.objects.filter(category__slug=category_slug)
    print(products_by_category)
    return products_by_category


def get_user_bookmarks_q(user: User) -> QuerySet[ProductBookmark]:
    product_bookmarks = ProductBookmark.objects.filter(user=user)
    return product_bookmarks


def get_user_orders_q(user: User) -> QuerySet[Order]:
    return Order.objects.filter(customer=user)
