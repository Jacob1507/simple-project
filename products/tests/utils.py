from typing import Optional, List, Union, Tuple

from django.contrib.auth import get_user_model

from products.models import Category, Product, ProductBookmark, User

AuthUser = get_user_model()


def create_user(username: str, password: str = "1234") -> User:
    AuthUser.objects.create(username=username, password=password)
    mongo_doc = User.objects.create(username=username)
    return mongo_doc


def create_categories(
    category_names: Union[List[str], Tuple[str]] = ("Test Category",)
) -> Union[List[Category], Tuple[Category]]:
    categories = list()
    for name in category_names:
        cat = Category.objects.create(name=name)
        categories.append(cat)
    return categories


def create_product(
    name: str,
    price: float = 99.99,
    description: str = "FooBar",
    categories: Optional[List[Category]] = None,
) -> Product:
    if categories is None:
        categories = create_categories()
    return Product.objects.create(
        name=name, price=price, description=description, categories=categories
    )


def create_product_bookmark(user: User, product: Product) -> ProductBookmark:
    return ProductBookmark.objects.create(user=user, product=product)
