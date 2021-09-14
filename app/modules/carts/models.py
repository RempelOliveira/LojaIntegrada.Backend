from datetime import datetime
from mongoengine import Document, ReferenceField, DateTimeField


class Cart(Document):
    discount_coupon = ReferenceField("Coupon")
    created_at = DateTimeField(required=True, default=datetime.utcnow)

    meta = {
        "collection": "carts"
    }
