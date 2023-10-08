from django.db.models import QuerySet

from products.models import User
from orders.models import Order


def get_user_orders_q(user: User) -> QuerySet[Order]:
    return Order.objects(customer=user)
