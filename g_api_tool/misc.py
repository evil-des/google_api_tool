import json
from g_api_tool.classes.CurrencyAPI import CurrencyAPI
from sqlalchemy import inspect

with open("config/config.json") as json_data:
    config = json.load(json_data)

currency_api = CurrencyAPI()


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}
