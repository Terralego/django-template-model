from tempfile import TemporaryDirectory

from django.template.loader import render_to_string
from django.test import TestCase, override_settings

from template_model.tests.factories import TemplateHTMLFactory


@override_settings(MEDIA_ROOT=TemporaryDirectory().name)
class LoaderTestCase(TestCase):
    def setUp(self) -> None:
        pass

    def test_template_found(self):
        # create a template in db
        my_template = TemplateHTMLFactory()
        self.maxDiff = None
        # try to render this template
        data = {
            'properties': {
                "name": "Test",
                "city": "Here",
                "description": "About ?",
                "access": "By there"
            }
        }
        rendered_content = render_to_string(my_template.template_file.name,
                                            context={
                                                "object": data
                                            })

        for key in data['properties']:
            self.assertIn(data['properties'][key], rendered_content)
