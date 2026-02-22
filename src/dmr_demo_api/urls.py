from django.urls import include, path

from dmr.errors import build_404_handler
from dmr.routing import Router
from dmr_demo_api.apps.controllers import urls as controllers_urls
from dmr_demo_api.apps.django_session_auth import urls as django_session_auth_urls
from dmr_demo_api.apps.jwt_auth import urls as jwt_auth_urls
from dmr_demo_api.apps.middlewares import urls as middleware_urls
from dmr_demo_api.apps.models_example import urls as models_example_urls
from dmr_demo_api.apps.negotiations import urls as negotiations_urls
from dmr_demo_api.apps.openapi.urls import build_spec

router = Router([
    path(
        'model-examples/',
        include(
            (models_example_urls.router.urls, 'models_example'),
            namespace='model_examples',
        ),
    ),
    path(
        'middlewares/',
        include(
            (middleware_urls.router.urls, 'middlewares'),
            namespace='middlewares',
        ),
    ),
    path(
        'controllers/',
        include(
            (controllers_urls.router.urls, 'controllers'),
            namespace='controllers',
        ),
    ),
    path(
        'negotiations/',
        include(
            (negotiations_urls.router.urls, 'negotiations'),
            namespace='negotiations',
        ),
    ),
    path(
        'jwt-auth/',
        include(
            (jwt_auth_urls.router.urls, 'jwt_auth'),
            namespace='jwt_auth',
        ),
    ),
    path(
        'django-session-auth/',
        include(
            (django_session_auth_urls.router.urls, 'django_session_auth'),
            namespace='django_session_auth',
        ),
    ),
])

urlpatterns = [
    path('api/', include((router.urls, 'server'), namespace='api')),
    path('docs/', build_spec(router)),
]

handler404 = build_404_handler('api/')
