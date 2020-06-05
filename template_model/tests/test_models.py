from tempfile import gettempdir

from django.test import TestCase, override_settings

from template_model.tests.factories import TemplateHTMLFactory


@override_settings(MEDIA_ROOT=gettempdir())
class TemplateModelTestCase(TestCase):
    def setUp(self):
        self.template = TemplateHTMLFactory()

    def test_template_str(self):
        self.assertEqual(str(self.template),
                         self.template.name)
