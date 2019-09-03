from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from ..serializers import TemplateSerializer
from .settings import ODT_TEMPLATE_PATH


class TestSerializers(TestCase):

    def test_template_serializer_with_file(self):
        b_content = open(ODT_TEMPLATE_PATH, 'rb').read()
        f = SimpleUploadedFile(
            'template.odt',
            b_content,
            content_type='application/vnd.oasis.opendocument.text',
        )
        serializer = TemplateSerializer(data={'name': 'Template', 'template_file': f})
        self.assertTrue(serializer.is_valid(), serializer.errors)
        self.assertTrue('content' not in serializer.validated_data)
        self.assertEqual(serializer.validated_data['name'], 'Template')
        self.assertEqual(
            serializer.validated_data['template_file'].read(),
            b_content,
        )

    def test_template_serializer_with_content(self):
        serializer_data = {
            'name': 'Template',
            'content': 'Hello world!'
        }
        serializer = TemplateSerializer(data=serializer_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        self.assertTrue('content' not in serializer.validated_data)
        self.assertEqual(serializer.validated_data['name'], 'Template')
        self.assertEqual(
            serializer.validated_data['template_file'].read(),
            'Hello world!',
        )

    def test_template_serializer_with_content_and_file(self):
        b_content = open(ODT_TEMPLATE_PATH, 'rb').read()
        f = SimpleUploadedFile(
            'template.odt',
            b_content,
            content_type='application/vnd.oasis.opendocument.text',
        )
        serializer = TemplateSerializer(
            data={'name': 'Template', 'template_file': f, 'content': 'Hello world!'})
        self.assertFalse(serializer.is_valid())

    def test_template_serializer_with_no_content_and_no_file(self):
        serializer = TemplateSerializer(data={'name': 'Template'})
        self.assertFalse(serializer.is_valid())
