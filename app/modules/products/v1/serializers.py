from flask_restful import fields


class ProductsSerializers:
    def input_data():
        return {
            "product_uuid": {
                "type": "string",
                "empty": False,
                "required": True,
                "instance_of_uuid": True
            },
            "price": {
                "type": "float",
                "empty": False,
                "required": True
            },
            "amount": {
                "type": "integer",
                "empty": False,
                "required": True
            }
        }

    def output_data():
        return {
            "id": fields.String,
            "products": fields.List(
                fields.Nested({
                    "id": fields.String,
                    "price": fields.Float,
                    "amount": fields.Integer
                })
            )
        }

class ProductSerializers:
    def input_data():
        return {
            "price": {
                "type": "float",
                "empty": False
            },
            "amount": {
                "type": "integer",
                "empty": False
            }
        }
