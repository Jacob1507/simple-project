from django.test import TestCase
from django.contrib.auth import get_user_model

from products.models import Category, Product, ProductBookmark, Order, OrderDetail
from products import logic as product_logic


User = get_user_model()


class ProductTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.customer1 = User.objects.create(
            username="test customer1",
            password="1234",
        )
        cls.customer2 = User.objects.create(
            username="test customer2",
            password="1234",
        )

        cls.category = Category.objects.create(
            name="Sport",
            slug="sport",
        )

        cls.prod1 = Product.objects.create(
            name="Rower1",
            price=999.9,
            description="test product1",
            category=cls.category,
        )
        cls.prod2 = Product.objects.create(
            name="Rower2",
            price=1000.0,
            description="test product2",
            category=cls.category,
        )
        cls.prod3 = Product.objects.create(
            name="Rower3",
            price=5999.9,
            description="test product3",
            category=cls.category,
        )

        cls.user_prod_bookmark1 = ProductBookmark.objects.create(
            user=cls.customer1,
            product=cls.prod1,
        )
        cls.user_prod_bookmark3 = ProductBookmark.objects.create(
            user=cls.customer2,
            product=cls.prod1,
        )
        cls.user_prod_bookmark4 = ProductBookmark.objects.create(
            user=cls.customer2, product=cls.prod3
        )

    def test_returns_products_by_category(self):
        prod_q = product_logic.get_products_q(category_slug=self.category.slug)
        self.assertTrue(self.prod1 in prod_q)

    def test_user_bookmarks(self):
        user_bkmrk_q = product_logic.get_user_bookmarks_q(user=self.customer1)
        self.assertTrue(self.user_prod_bookmark1 in user_bkmrk_q)

    def test_order(self):
        order_detail = OrderDetail.objects.create(
            city="Warszawa",
            street="Random street",
            postal_code="11-111",
        )
        new_order = Order.objects.create(
            customer=self.customer1,
            product=self.prod1,
            order_detail=order_detail,
        )
        self.assertTrue(
            new_order in product_logic.get_user_orders_q(user=self.customer1)
        )
