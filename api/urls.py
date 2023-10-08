from django.urls import path

from api.views import ProductsListView, CategoryListView, ProductBookmarkListView

urlpatterns = [
    path("products/", ProductsListView.as_view(), name="product-list"),
    path("categories/", CategoryListView.as_view(), name="categories-list"),
    path(
        "product-bookmarks",
        ProductBookmarkListView.as_view(),
        name="prod-bookmarks-list",
    ),
]
