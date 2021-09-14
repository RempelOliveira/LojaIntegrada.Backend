from mongoengine import DoesNotExist
from app.modules.coupons.models import Coupon


class CouponRepository:
    def __new__(self, **kwargs):
        return Coupon(**kwargs)

    def find_one(**kwargs):
        try:
            return Coupon.objects.get(**kwargs)
        except DoesNotExist:
            return None
