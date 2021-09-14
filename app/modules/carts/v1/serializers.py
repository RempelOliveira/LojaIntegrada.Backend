from flask_restful import fields


class CartSerializers:
    def input_data():
        return {
            "product_uuid": {
                "type": "string",
                "required": True,
                "instance_of_uuid": True
            },
            "price": {
                "type": "float"
            },
            "amount": {
                "type": "integer"
            }
        }

    def output_data(complete_resource=False):
        if not complete_resource:
            return {
                "id": fields.String,
                "products": fields.List(
                    fields.Nested({
                        "id": fields.String,
                        "price": fields.Float,
                        "amount": fields.Integer,
                    })
                )
            }

        else:
            return {
                "id": fields.String,
                "discount": fields.Nested({
                    "type": fields.String,
                    "value": fields.Float
                }),
                "products": fields.List(
                    fields.Nested({
                        "id": fields.String,
                        "title": fields.String,
                        "description": fields.String,
                        "price": fields.Float,
                        "amount": fields.Integer,
                        "image": fields.String
                    })
                ),
                "total": fields.Float,
                "subtotal": fields.Float
            }
