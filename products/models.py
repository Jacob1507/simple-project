from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name")),
    price = models.FloatField(verbose_name=_("Price"))
    description = models.CharField(max_length=500, verbose_name=_("Description"))

    def __str__(self):
        return self.name


class ProductBookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Customer"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))


class ProductCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Category name"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Customer"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    ordered_at = models.DateTimeField(verbose_name=_("Order date"))
