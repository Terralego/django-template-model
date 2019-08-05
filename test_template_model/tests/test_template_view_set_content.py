import os

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

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
        self.template = Template.objects.create(
            name='Template',
            format='odt',
            content=from_bytes_to_str(
                open(os.path.join('test_template_model', 'tests', 'template.odt'), 'rb').read(),
                'odt'
            ),
            object_id=self.object.pk,
            content_type=ContentType.objects.get_for_model(Bidon),
        )

    def test_content_works(self):
        response = self.client.get(reverse('template-content', kwargs={'pk': self.object.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.content,
            open(os.path.join('test_template_model', 'tests', 'template.odt'), 'rb').read()
        )

    def test_content_bad_pk(self):
        response = self.client.get(reverse('template-content', kwargs={'pk': self.object.pk + 1}))
        self.assertEqual(response.status_code, 404)


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
