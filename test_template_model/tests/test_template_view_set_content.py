import json
import os

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.core.files.uploadedfile import SimpleUploadedFile

from template_model.utils import from_bytes_to_str
from template_model.models import Template

from test_template_model.models import Bidon

UserModel = get_user_model()


class TestOdtTemplateViewSetContent(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user('michel', 'michel')
        self.client.login(**{'username': 'michel', 'password': 'michel'})
        self.object = Bidon.objects.create(name='Composantes')

    def test_content_works(self):
        f = SimpleUploadedFile(
            'template.odt',
            open(os.path.join('test_template_model', 'tests', 'template.odt'), 'rb').read(),
            content_type='application/vnd.oasis.opendocument.text',
        )
        bidon_model_content_type_pk = ContentType.objects.get_for_model(Bidon).pk
        post_response = self.client.post(
            reverse('template-list'),
            data={
                'name': 'Template',
                'format': 'odt',
                'content': f,
                'object_id': self.object.pk,
                'content_type': bidon_model_content_type_pk,
            }
        )
        self.assertEqual(post_response.status_code, 201)
        template_info = json.loads(
            post_response.content.decode()
        )
        self.assertEqual(template_info['name'], 'Template')
        self.assertEqual(template_info['format'], 'odt')
        self.assertEqual(template_info['content_type'], bidon_model_content_type_pk)
        self.assertEqual(template_info['object_id'], self.object.pk)

        response = self.client.get(reverse('template-content', kwargs={'pk': self.object.pk}))
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
        self.object = Bidon.objects.create(name='Composantes')
        self.template = Template.objects.create(
            name='Template',
            format='docx',
            content=from_bytes_to_str(
                open(os.path.join('test_template_model', 'tests', 'template.docx'), 'rb').read(),
                'docx'
            ),
            object_id=self.object.pk,
            content_type=ContentType.objects.get_for_model(Bidon),
        )

    def test_content_works(self):
        response = self.client.get(reverse('template-content', kwargs={'pk': self.object.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.content,
            open(os.path.join('test_template_model', 'tests', 'template.docx'), 'rb').read()
        )

    def test_content_bad_pk(self):
        response = self.client.get(reverse('template-content', kwargs={'pk': self.object.pk + 1}))
        self.assertEqual(response.status_code, 404)
