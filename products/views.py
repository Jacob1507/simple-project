from django.shortcuts import render

from .logic import get_products_q


def product_list(request):
    products_q = get_products_q()
    context = dict(products=products_q)
    return render(request, "products_list.html", context)
