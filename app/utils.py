import json

from flask import request
from collections.abc import Mapping


def merge_attrs(data, attrs):
    for key, value in attrs.items():
        if isinstance(data.get(key), dict) and isinstance(value, Mapping):
            merge_attrs(data[key], value)
        else:
            data[key] = value

    return data


def get_json_request():
    def parse_json(data):
        for key, value in data.items():
            if isinstance(value, str):
                try:
                    data[key] = json.loads(value, parse_int=str)
                except Exception:
                    pass

        return data

    def strip_attrs(json_data):
        if type(json_data) not in [str, dict]:
            return json_data

        data = {}

        for k, v in json_data.items():
            if isinstance(v, str):
                data[k] = v.strip() if v.strip() != "" else v
            else:
                data[k] = strip_attrs(v)

        return data

    if request.is_json:
        try:
            json_data = request.json
        except Exception:
            json_data = None
    else:
        json_data = parse_json(request.form.to_dict())

    return strip_attrs(json_data) or {}
