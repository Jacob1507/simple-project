from datetime import timedelta

from django.utils import timezone

from products.tests import utils as product_testutils
from orders.tests import utils as order_testutils
from orders import logic as order_logic
from utils.test import MongoTestCaseHelper


class BasicOrderTest(MongoTestCaseHelper):
    @classmethod
    def setUpTestData(cls):
        cls.user = product_testutils.create_user(username="Customer")
        cls.product = product_testutils.create_product(name="Test product")

    def test_order_list_empty(self):
        order_q = order_logic.get_user_orders_q(user=self.user)
        self.assert_list_result(order_q, [])

    def test_add_order(self):
        dt = timezone.now() - timedelta(hours=12)
        order_detail = order_testutils.OrderData(
            city="Random city",
            street="Random street 99",
            postal_code="00-000",
            ordered_at=dt,
        )
        order = order_testutils.create_order(
            customer=self.user, product=self.product, order_data=order_detail
        )
        order_q = order_logic.get_user_orders_q(user=self.user)
        self.assert_list_result(order_q, [order])
        self.assertEqual(order.order_detail.ordered_at, dt)
