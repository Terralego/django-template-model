from django.urls import include, path
from rest_framework import routers

from .views import TemplateViewSet

router = routers.SimpleRouter()
router.register(r'document-template', TemplateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
