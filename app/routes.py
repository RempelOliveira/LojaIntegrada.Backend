from app.modules.carts.v1.controllers import Cart
from app.modules.products.v1.controllers import Product, Products
from app.modules.coupons.v1.controllers import Coupon


def load_routes(api):
    api.add_resource(Cart,
        "/v1/cart",
        "/v1/cart/<string:cart_id>")

    api.add_resource(Product,
        "/v1/cart/<string:cart_id>/products/<string:product_id>")

    api.add_resource(Products,
        "/v1/cart/<string:cart_id>/products")

    api.add_resource(Coupon,
        "/v1/cart/<string:cart_id>/coupon")
