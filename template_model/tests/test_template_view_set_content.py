import os
import json

from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase

from ..models import Template
from .settings import ODT_TEMPLATE_PATH, DOCX_TEMPLATE_PATH

UserModel = get_user_model()


def remove_template_file(template_info):
    f = Template.objects.get(pk=template_info['pk']).template_file
    os.remove(f.path)


class TestTemplateViewSetContent(APITestCase):

    def setUp(self):
        self.user = UserModel.objects.create(username='michel')
        self.client.force_authenticate(user=self.user)

    def test_content_with_odt_file(self):
        up_file = SimpleUploadedFile(
            'template.odt',
            open(ODT_TEMPLATE_PATH, 'rb').read(),
            content_type='application/vnd.oasis.opendocument.text',
        )
        post_response = self.client.post(
            reverse('template-list'),
            data={
                'name': 'Template',
                'template_file': up_file,
            },
        )
        template_info = json.loads(
            post_response.content.decode()
        )
        self.assertEqual(post_response.status_code, 201)
        self.assertEqual(template_info['name'], 'Template')
        response = self.client.get(
            reverse('template-content', kwargs={'pk': template_info['pk']}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            b''.join(response.streaming_content),
            open(ODT_TEMPLATE_PATH, 'rb').read()
        )
        remove_template_file(template_info)

    def test_content_with_docx_file(self):
        f = SimpleUploadedFile(
            'template.docx',
            open(DOCX_TEMPLATE_PATH, 'rb').read(),
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        )
        post_response = self.client.post(
            reverse('template-list'),
            data={
                'name': 'Template',
                'template_file': f,
            }
        )
        template_info = json.loads(
            post_response.content.decode()
        )
        self.assertEqual(post_response.status_code, 201)
        self.assertEqual(template_info['name'], 'Template')

        response = self.client.get(
            reverse('template-content', kwargs={'pk': template_info['pk']}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            b''.join(response.streaming_content),
            open(DOCX_TEMPLATE_PATH, 'rb').read()
        )
        remove_template_file(template_info)

    def test_content_with_text(self):
        post_response = self.client.post(
            reverse('template-list'),
            data={
                'name': 'Template',
                'content': 'Hello world!',
            },
        )
        template_info = json.loads(
            post_response.content.decode()
        )
        self.assertEqual(post_response.status_code, 201)
        self.assertEqual(template_info['name'], 'Template')
        response = self.client.get(
            reverse('template-content', kwargs={'pk': template_info['pk']}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            b''.join(response.streaming_content),
            b'Hello world!'
        )
        remove_template_file(template_info)
