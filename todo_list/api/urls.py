from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TodoViewSet

router_v1 = DefaultRouter()

router_v1.register('create', TodoViewSet),
router_v1.register('get/(?P<uuid>\\d+)', TodoViewSet)
router_v1.register('all', TodoViewSet),
router_v1.register('list/(?P<created>\\d+)', TodoViewSet),
router_v1.register('delite/(?P<uuid>\\d+)', TodoViewSet)

urlpatterns = [ 
    path('record/', include(router_v1.urls)),
]
