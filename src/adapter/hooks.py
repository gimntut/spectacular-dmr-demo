from collections.abc import Sequence

from django.urls import URLResolver, URLPattern
from dmr.openapi.views import OpenAPIView
from drf_spectacular.generators import SchemaGenerator


def dmr_adapter_hook(*, result: dict, generator: SchemaGenerator, **_kwargs) -> dict:
    patterns = _get_patterns(generator.inspector.patterns)
    schemas = []
    schema_ids = set()
    for pattern in patterns:
        view = pattern.callback
        if not hasattr(view, 'view_class') or not issubclass(view.view_class, OpenAPIView):
            continue
        schema = view.view_initkwargs['schema']
        schema_id = id(schema)
        if schema_id not in schema_ids:
            schemas.append(schema)
            schema_ids.add(schema_id)
    return _merge_dicts(result, schemas[0])


def _get_patterns(patterns: Sequence[URLPattern | URLResolver]) -> list[URLPattern]:
    flat_patterns = []
    for pattern in patterns:
        if isinstance(pattern, URLResolver):
            flat_patterns.extend(_get_patterns(pattern.url_patterns))
        else:
            flat_patterns.append(pattern)
    return flat_patterns


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
