from mongoengine import Document, EmbeddedDocument, \
    StringField, DecimalField, DateTimeField, EmbeddedDocumentField

from app.constants import DISCOUNT_TYPES


class Discount(EmbeddedDocument):
    type = StringField(required=True, choices=DISCOUNT_TYPES)
    value = DecimalField(required=True)

class Coupon(Document):
    code = StringField(required=True, unique=True)
    discount = EmbeddedDocumentField("Discount", required=True)
    expires_at = DateTimeField(required=True)

    meta = {
        "collection": "coupons"
    }
