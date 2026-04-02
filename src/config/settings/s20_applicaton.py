from .s10_django_default import INSTALLED_APPS as DJANGO_APPS

THIRD_PARTY_APPS = [
    "rest_framework",
    "drf_spectacular",
    "django_extensions",
    "dmr.apps.DjangoModernRestConfig",
]
APP_APPS = [
    "drf_api.apps.DrfConfig",
    "dmr_demo_api.apps.models_example",
    "dmr_demo_api.apps.middlewares",
    "dmr_demo_api.apps.controllers",
    "dmr_demo_api.apps.openapi",
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + APP_APPS

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ],
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Demo DRF + DMR",
    "DESCRIPTION": (
        "Demonstration of the possibilities of combining the DRF and DMR APIs\n\n"
        "Other pages:\n"
        "* [DMR Swagger](/docs/swagger/)\n"
        "* [DMR Redoc](/docs/redoc/)\n"
        "* [DMR Scalar](/docs/scalar/)\n"
        "* [DMR Stoplight](/docs/stoplight/)"
    ),
    "VERSION": "0.4.0",
    "SERVE_INCLUDE_SCHEMA": False,
    # !!! This is where the adapter is connected !!!
    # !!! Вот здесь происходит подключение адаптера !!!
    "POSTPROCESSING_HOOKS": ["adapter.hooks.dmr_adapter_hook"],
}
