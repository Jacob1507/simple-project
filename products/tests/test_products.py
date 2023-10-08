from products.tests import utils as product_testutils
from products import logic as product_logic
from utils.test import MongoTestCaseHelper


class BasicProductsTest(MongoTestCaseHelper):
    @classmethod
    def setUpTestData(cls):
        cls.user = product_testutils.create_user(username="Customer")
        cls.category_list = product_testutils.create_categories(category_names=["cat1"])
        cls.product = product_testutils.create_product(name="Test product")

    def test_category_list_empty(self):
        category_q = product_logic.get_category_q()
        self.assert_list_result(category_q, [])

    def test_user_bookmarks_list_empty(self):
        bookmarks_q = product_logic.get_user_bookmarks_q(user=self.user)
        self.assert_list_result(bookmarks_q, [])

    def test_product_list_empty(self):
        product_q = product_logic.get_products_q(categories=self.category_list)
        self.assert_list_result(product_q, [])

    def test_product_added(self):
        prod = product_testutils.create_product(
            name="product 1", categories=self.category_list
        )
        product_q = product_logic.get_products_q(categories=self.category_list)
        self.assert_list_result(product_q, [prod], prod.categories)

    def test_product_has_two_categories(self):
        new_category = product_testutils.create_categories(category_names=["cat2"])
        self.product.categories.append(new_category)
        self.assertEqual(len(self.product.categories), 2)
