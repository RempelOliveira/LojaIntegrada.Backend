from flask_restful import fields


class CouponSerializers:
    def input_data():
        return {
            "code": {
                "type": "string",
                "empty": False,
                "required": True
            }
        }

    def output_data():
        return {
            "type": fields.String(attribute=lambda v: v["discount"]["type"]),
            "value": fields.Float(attribute=lambda v: v["discount"]["value"]),
            "expires_at": fields.DateTime
        }
