from typing import Optional, List

from django.db.models import QuerySet

from products.models import Category, Product, ProductBookmark, User


def get_category_q() -> QuerySet[Category]:
    return Category.objects()


def get_products_q(categories: List[Optional[Category]] = None) -> QuerySet[Product]:
    """Returns products by categories"""
    query = Product.objects()
    if categories:
        query = query(categories__in=categories)
    return query


def get_user_bookmarks_q(user: User) -> QuerySet[ProductBookmark]:
    return ProductBookmark.objects(user=user)
