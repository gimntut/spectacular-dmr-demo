from dmr.openapi import build_schema

from dmr_demo_api.apps.openapi.config import get_config
from dmr_demo_api.urls import router


def dmr_adapter_hook(*, result: dict, generator, **_kwargs) -> dict:
    openapi_schema = build_schema(router, config=get_config())
    schema = openapi_schema.convert()
    return _merge_dicts(result, schema)


def _merge_dicts(data_1: dict, data_2: dict) -> dict:
    result = {}
    keys = set()
    for key, value in data_1.items():
        if key not in data_2:
            result[key] = value
        elif isinstance(value, dict) and isinstance(data_2[key], dict):
            result[key] = _merge_dicts(value, data_2[key])
        elif isinstance(value, list) and isinstance(data_2[key], list):
            result[key] = value + data_2[key]
        else:
            result[key] = value
        keys.add(key)
    for key, value in data_2.items():
        if key not in keys:
            result[key] = value
    return result
