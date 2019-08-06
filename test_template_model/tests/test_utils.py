from django.test import TestCase

from template_model.utils import from_bytes_to_str, from_str_to_bytes


class TestUtils(TestCase):

    def test_from_bytes_to_str_html(self):
        self.assertEqual('Hello!', from_bytes_to_str(b'Hello!', 'html'))

    def test_from_bytes_to_str_odt(self):
        self.assertEqual('SGVsbG8h', from_bytes_to_str(b'Hello!', 'odt'))

    def test_from_bytes_to_str_bad_format(self):
        self.assertEqual(None, from_bytes_to_str(b'Hello!', 'michel'))

    def test_from_str_to_bytes_html(self):
        self.assertEqual(b'Hello!', from_str_to_bytes('Hello!', 'html'))

    def test_from_str_to_bytes_odt(self):
        self.assertEqual(b'Hello!', from_str_to_bytes('SGVsbG8h', 'odt'))

    def test_from_str_to_bytes_bad_format(self):
        self.assertEqual(None, from_str_to_bytes('SGVsbG8h', 'michel'))
