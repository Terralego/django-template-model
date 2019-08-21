import json
import os

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

from template_model.utils import from_bytes_to_str
from template_model.models import Template

UserModel = get_user_model()


class TestOdtTemplateViewSetContent(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user('michel', 'michel')
        self.client.login(**{'username': 'michel', 'password': 'michel'})

    def test_content_works(self):
        f = SimpleUploadedFile(
            'template.odt',
            open(os.path.join('test_template_model', 'tests', 'template.odt'), 'rb').read(),
            content_type='application/vnd.oasis.opendocument.text',
        )
        post_response = self.client.post(
            reverse('template-list'),
            data={
                'name': 'Template',
                'format': 'odt',
                'content': f,
            }
        )
        self.assertEqual(post_response.status_code, 201)
        template_info = json.loads(
            post_response.content.decode()
        )
        self.assertEqual(template_info['name'], 'Template')
        self.assertEqual(template_info['format'], 'odt')

        response = self.client.get(reverse('template-content', kwargs={'pk': template_info['id']}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.content,
            open(os.path.join('test_template_model', 'tests', 'template.odt'), 'rb').read()
        )


class TestDocxTemplateViewSetContent(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user('michel', 'michel')
        self.client.login(**{'username': 'michel', 'password': 'michel'})
        self.template = Template.objects.create(
            name='Template',
            format='docx',
            content=from_bytes_to_str(
                open(os.path.join('test_template_model', 'tests', 'template.docx'), 'rb').read(),
                'docx'
            ),
        )

    def test_content_works(self):
        response = self.client.get(reverse('template-content', kwargs={'pk': self.template.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.content,
            open(os.path.join('test_template_model', 'tests', 'template.docx'), 'rb').read()
        )
