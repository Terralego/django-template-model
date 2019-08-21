import os

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from template_model.forms import TemplateForm
from template_model.utils import from_bytes_to_str


class TestForms(TestCase):

    def test_template_form_works(self):
        b_content = open(os.path.join('test_template_model', 'tests', 'template.odt'), 'rb').read()
        f = SimpleUploadedFile(
            'template.odt',
            b_content,
            content_type='application/vnd.oasis.opendocument.text',
        )
        form_data = {
            'name': 'Template',
            'format': 'odt',
        }
        form = TemplateForm(data=form_data, files={'content': f})
        form.is_valid()
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['name'], 'Template')
        self.assertEqual(form.cleaned_data['format'], 'odt')
        self.assertEqual(
            form.cleaned_data['content'],
            from_bytes_to_str(b_content, 'odt')
        )
