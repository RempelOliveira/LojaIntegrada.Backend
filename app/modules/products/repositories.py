from mongoengine import DoesNotExist
from app.modules.products.models import Product


class ProductRepository:
    def __new__(self, **kwargs):
        return Product(**kwargs)

    def find(**kwargs):
        return Product.objects(**kwargs)

    def find_one(**kwargs):
        try:
            return Product.objects.get(**kwargs)
        except DoesNotExist:
            return None
