import os
import requests

from app.utils import merge_attrs


class ProductServices:
    def retrieve_products(products):
        try:
            uuids = []

            for product in products:
                uuids.append(f'uuids[]={product.product_uuid}')

            response = requests.get(f'{os.getenv("X_API")}/v1/products?{"&".join(uuids)}',
                headers={
                    "X-API-KEY": os.getenv("X_API_KEY")
                }
            )

        except Exception:
            return None

        products_list = []

        for product in response.json()["products"]:
            for _product in products:
                if str(_product.product_uuid) == product["id"]:
                    products_list.append(merge_attrs(product, {
                        "price": _product.price, "amount": _product.amount
                    }))

        return products_list
