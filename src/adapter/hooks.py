from collections.abc import MutableMapping

from dmr.openapi import build_schema
from mergedeep import merge

from dmr_demo_api.apps.openapi.config import get_config
from dmr_demo_api.urls import router


def dmr_adapter_hook(*, result: dict, generator, **_kwargs) -> MutableMapping:
    openapi_schema = build_schema(router, config=get_config())
    schema = openapi_schema.convert()
    return merge(schema, result)
