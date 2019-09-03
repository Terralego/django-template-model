from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from ..forms import TemplateForm
from .settings import ODT_TEMPLATE_PATH


class TestForms(TestCase):

    def test_template_form_with_file(self):
        b_content = open(ODT_TEMPLATE_PATH, 'rb').read()
        f = SimpleUploadedFile(
            'template.odt',
            b_content,
            content_type='application/vnd.oasis.opendocument.text',
        )
        form_data = {
            'name': 'Template',
        }
        form = TemplateForm(data=form_data, files={'template_file': f})
        self.assertTrue(form.is_valid(), form.errors)
        self.assertTrue('content' not in form.cleaned_data)
        self.assertEqual(form.cleaned_data['name'], 'Template')
        self.assertEqual(
            form.cleaned_data['template_file'].read(),
            b_content,
        )

    def test_template_form_with_content(self):
        form_data = {
            'name': 'Template',
            'content': 'Hello world!'
        }
        form = TemplateForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)
        self.assertTrue('content' not in form.cleaned_data)
        self.assertEqual(form.cleaned_data['name'], 'Template')
        self.assertEqual(
            form.cleaned_data['template_file'].read(),
            'Hello world!',
        )

    def test_template_form_with_content_and_file(self):
        b_content = open(ODT_TEMPLATE_PATH, 'rb').read()
        f = SimpleUploadedFile(
            'template.odt',
            b_content,
            content_type='application/vnd.oasis.opendocument.text',
        )
        form = TemplateForm(
            data={'name': 'Template', 'content': 'Hello world!'},
            files={'template_file': f}
        )
        self.assertFalse(form.is_valid())

    def test_template_form_with_no_content_and_no_file(self):
        form = TemplateForm(data={'name': 'Template'})
        self.assertFalse(form.is_valid())
