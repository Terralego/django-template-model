from rest_framework.serializers import FileField, ModelSerializer

from .models import Template
from .utils import FmtMimeMapping, from_bytes_to_str


class TemplateSerializer(ModelSerializer):
    content = FileField(write_only=True)

    class Meta:
        model = Template
        fields = '__all__'
        extra_kwargs = {
            'added': {'read_only': True},
            'updated': {'read_only': True},
        }

    def validate_content(self, data):
        fmt = FmtMimeMapping(data.content_type).name
        b_content = data.file.read()
        return from_bytes_to_str(b_content, fmt)
