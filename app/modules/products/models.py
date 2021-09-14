from mongoengine import Document, CASCADE, \
    ReferenceField, UUIDField, DecimalField, IntField


class Product(Document):
    cart = ReferenceField("Cart", required=True, reverse_delete_rule=CASCADE)
    product_uuid = UUIDField(required=True, unique_with="cart", binary=False)
    price = DecimalField(required=True)
    amount = IntField(required=True, default=1)

    meta = {
        "collection": "products"
    }
