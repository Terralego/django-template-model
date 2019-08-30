from django.test import TestCase

from template_model.models import Template


class TemplateModelTestCase(TestCase):
    def setUp(self):
        self.template = Template.objects.create(name='template', format='odt')

    def test_template_str(self):
        self.assertEqual(str(self.template), 'template (odt)')
