from django.db.models import QuerySet
from django.test import TestCase
from django.conf import settings
from rest_framework import status
from rest_framework.test import APIClient


class settings:
    MONGO_DATABASE_NAME = "dummy"
    MONGO_PORT = 27017


class MongoTestCase(TestCase):
    """
    TestCase class that clear the collection between the tests
    """

    mongodb_name = "test_%s" % settings.MONGO_DATABASE_NAME

    def _pre_setup(self):
        from mongoengine.connection import connect, disconnect

        disconnect()
        connect(self.mongodb_name, port=settings.MONGO_PORT)
        super()._pre_setup()

    def _post_teardown(self):
        from mongoengine.connection import get_connection, disconnect

        connection = get_connection()
        connection.drop_database(self.mongodb_name)
        disconnect()
        super()._post_teardown()


class HelperMongoTestCase(MongoTestCase):
    def assert_list_result(self, query: QuerySet, expected: list, msg: str = ""):
        """Compares query output with expected data"""
        self.assertListEqual(list(query), expected, msg)


class MongoAPITestCase(MongoTestCase):
    client_class = APIClient


class MongoHelperAPITestCase(MongoAPITestCase):
    def get_list_results(self, response):
        self.assertEqual(response.status_code, status.HTTP_200_OK, str(response.data))
        self.assertIsNotNone(response.data, str(response.data))
        return response.data

    def as_user(self, user, action):
        self.client.force_authenticate(user=user)
        result = action()
        self.client.force_authenticate(user=None)
        return result
