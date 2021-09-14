import os
import sys

from datetime import datetime, timedelta
from mongoengine import connect


sys.path += [os.getcwd()]


if __name__ == "__main__":
    from app.constants import DISCOUNT_TYPES
    from app.modules.coupons.repositories import CouponRepository

    try:
        with connect(os.getenv("MONGODB_NAME"), host=os.getenv("MONGODB_URL")) as conn:
            CouponRepository(**{
                "code": "AiJK9Y6F",
                "discount": {
                    "type": DISCOUNT_TYPES[0],
                    "value": 20
                },
                "expires_at": datetime.utcnow() + timedelta(days=2)
            }).save()

            CouponRepository(**{
                "code": "BcOY6A4d",
                "discount": {
                    "type": DISCOUNT_TYPES[1],
                    "value": 2.5
                },
                "expires_at": datetime.utcnow() + timedelta(days=3)
            }).save()

        print("== Seeds is ok")
    except Exception as e:
        print(str(e))
