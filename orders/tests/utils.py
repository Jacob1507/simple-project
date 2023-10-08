from datetime import datetime
from typing import NamedTuple

from django.utils import timezone

from products.models import User, Product
from orders.models import OrderDetail, Order


class OrderData(NamedTuple):
    city: str
    street: str
    postal_code: str
    ordered_at: datetime = timezone.now()


def create_order(customer: User, product: Product, order_data: OrderData) -> Order:
    order_detail = OrderDetail.objects.create(
        city=order_data.city,
        street=order_data.street,
        postal_code=order_data.postal_code,
        ordered_at=order_data.ordered_at,
    )
    return Order.objects.create(
        customer=customer, product=product, order_detail=order_detail
    )
