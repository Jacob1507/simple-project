from django.utils import timezone

from mongoengine import Document, fields, CASCADE


class User(Document):
    username = fields.StringField(max_length=50)
    first_name = fields.StringField(max_length=30)
    last_name = fields.StringField(max_length=30)


class Category(Document):
    name = fields.StringField(max_length=255)


class Product(Document):
    name = fields.StringField(max_length=255)
    price = fields.FloatField()
    description = fields.StringField(max_length=500)
    categories = fields.ListField(
        fields.ReferenceField("Category", reverse_delete_rule=CASCADE)
    )

    def __str__(self):
        return self.name


class ProductBookmark(Document):
    user = fields.ReferenceField("User", reverse_delete_rule=CASCADE)
    product = fields.ReferenceField("Product", reverse_delete_rule=CASCADE)
