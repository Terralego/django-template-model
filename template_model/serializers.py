from django.core.files.base import ContentFile
from django.utils.text import slugify
from rest_framework import serializers

from .models import Template


class TemplateSerializer(serializers.ModelSerializer):
    content = serializers.CharField(required=False, write_only=True)
    file = serializers.FileField(required=False, write_only=True)

    class Meta:
        model = Template
        fields = ('pk', 'name', 'mime_type', 'file', 'content', 'added', 'updated')
        extra_kwargs = {
            'mime_type': {'read_only': True},
            'added': {'read_only': True},
            'updated': {'read_only': True},
        }

    def validate(self, attrs):
        if 'content' in attrs and 'file' in attrs:
            raise serializers.ValidationError('You can not specify a text and upload a file.')
        elif 'content' not in attrs and 'file' not in attrs:
            raise serializers.ValidationError('Please specify a text or upload a file.')
        elif 'content' in attrs:
            attrs['file'] = ContentFile(attrs.pop('content'), name=slugify(attrs['name']))
        return attrs
