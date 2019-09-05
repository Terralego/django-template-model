from django.http import FileResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from .models import Template
from .serializers import TemplateSerializer


class TemplateViewSet(ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

    @action(detail=True, methods=['get'], url_path='content')
    def content(self, request, *args, **kwargs):
        template = self.get_object()
        return FileResponse(open(template.template_file.path, 'rb'), as_attachment=True)
