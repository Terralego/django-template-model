from django.forms import FileField, ModelForm

from .models import Template
from .utils import from_bytes_to_str


class TemplateForm(ModelForm):
    content = FileField()

    class Meta:
        model = Template
        fields = ['name', 'format', 'content', 'content_type', 'object_id']

    def clean_content(self):
        b_content = self.cleaned_data['content'].file.read()
        fmt = self.cleaned_data['format']
        return from_bytes_to_str(b_content, fmt)
