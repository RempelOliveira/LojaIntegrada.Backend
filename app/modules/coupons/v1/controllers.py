from datetime import datetime

from flask import request
from flask_restful import Resource, marshal

from app.decorators import validate_data

from app.modules.carts.repositories import CartRepository
from app.modules.coupons.repositories import CouponRepository

from app.modules.coupons.v1.serializers import CouponSerializers


class Coupon(Resource):
    @validate_data(CouponSerializers.input_data())
    def put(self, cart_id):
        data = request.data

        try:
            cart = CartRepository.find_one(id=cart_id)

            if not cart:
                return {"errors": "Cart not found"}, 404

            coupon = CouponRepository.find_one(
                code=data["code"], expires_at__gte=datetime.utcnow())

            if not coupon:
                return {"errors": "Coupon expired or not found"}, 404

            cart.update(discount_coupon=coupon)

        except Exception as e:
            return {"errors": str(e)}, 500

        return marshal(coupon, CouponSerializers.output_data()), 201

    def delete(self, cart_id):
        try:
            cart = CartRepository.find_one(id=cart_id)

            if not cart:
                return {"errors": "Cart not found"}, 404

            cart.update(unset__discount_coupon=True)

        except Exception as e:
            return {"errors": str(e)}, 500

        return None, 204
