from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TodoCreate, TodoDelete

router = DefaultRouter()

router.register('create', TodoCreate),
router.register('get/(?P<uuid>\\d+)', TodoCreate)
router.register('all', TodoCreate),
router.register('list/(?P<created>\\d+)', TodoCreate),
router.register('delete/(?P<uuid>\\d+)', TodoDelete)

urlpatterns = [ 
    path('record/', include(router.urls)),
]
