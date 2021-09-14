from mongoengine import DoesNotExist
from app.modules.carts.models import Cart


class CartRepository:
    def __new__(self, **kwargs):
        return Cart(**kwargs)

    def find_one(**kwargs):
        try:
            return Cart.objects.get(**kwargs)
        except DoesNotExist:
            return None
