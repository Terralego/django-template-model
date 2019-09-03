import os

from django.core.files import File
from django.test import TestCase

from template_model.models import Template

from .settings import ODT_TEMPLATE_PATH


class TemplateModelTestCase(TestCase):
    def setUp(self):
        self.file = File(open(ODT_TEMPLATE_PATH, 'rb'))
        self.template = Template.objects.create(name='template', template_file=self.file)

    def test_template_str(self):
        self.assertEqual(str(self.template),
                         'template (application/vnd.oasis.opendocument.text)')

    def test_save(self):
        self.assertEqual(
            'application/vnd.oasis.opendocument.text',
            self.template.mime_type)

    def tearDown(self):
        os.remove(self.template.template_file.path)
