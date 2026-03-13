from django.urls import path

from dmr.routing import Router
from dmr_demo_api.apps.negotiations import views

router = Router(
    'negotiations/',
    [
        path(
            'negotiation/',
            views.ContentNegotiationController.as_view(),
            name='negotiation',
        ),
    ],
)
