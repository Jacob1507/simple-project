from django.utils import timezone

from mongoengine import CASCADE, Document, fields


class OrderDetail(Document):
    city = fields.StringField(max_length=80)
    street = fields.StringField(max_length=80)
    postal_code = fields.StringField(max_length=6)
    ordered_at = fields.DateTimeField(default=timezone.now())


class Order(Document):
    customer = fields.ReferenceField("User", reverse_delete_rule=CASCADE)
    product = fields.ReferenceField("Product", reverse_delete_rule=CASCADE)
    order_detail = fields.ReferenceField("OrderDetail", reverse_delete_rule=CASCADE)
