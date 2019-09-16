from tempfile import gettempdir

from django.core.files import File
from django.test import TestCase, override_settings

from template_model.models import Template

from .settings import ODT_TEMPLATE_PATH


@override_settings(MEDIA_ROOT=gettempdir())
class TemplateModelTestCase(TestCase):
    def setUp(self):
        self.file = File(open(ODT_TEMPLATE_PATH, 'rb'))
        self.template = Template.objects.create(name='template', template_file=self.file)

    def test_template_str(self):
        self.assertEqual(str(self.template),
                         self.template.name)
