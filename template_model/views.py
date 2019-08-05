from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from .models import Template
from .serializers import TemplateSerializer
from .utils import FmtMimeMapping, from_str_to_bytes


class TemplateViewSet(ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

    @action(detail=True, methods=['get'], url_path='content')
    def content(self, request, *args, **kwargs):
        obj = self.get_object()
        return HttpResponse(
            content=from_str_to_bytes(obj.content, obj.format),
            content_type=getattr(FmtMimeMapping, obj.format).value
        )
