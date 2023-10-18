from django.urls import reverse

from products.tests import utils as product_testutils
from utils.test import MongoHelperAPITestCase


class ProductsTests(MongoHelperAPITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = product_testutils.create_user(username="Test User")
        cls.product_list_url = reverse("product-list")

    def test_product_list_empty(self):
        response = self.as_user(
            self.user, lambda: self.client.get(self.product_list_url)
        )
        result = self.get_list_results(response)
        self.assertEqual(result, [])

    def test_post_new_product(self):
        pass
