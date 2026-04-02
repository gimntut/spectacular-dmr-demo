from dmr.routing import Router, path
from dmr_demo_api.apps.models_example import views

router = Router(
    'model-examples/',
    [
        path(
            'user/',
            views.UserCreateController.as_view(),
            name='user_model_create',
        ),
    ],
)
