from django import forms
from django.utils.text import slugify
from django.core.files.base import ContentFile

from .models import Template


class TemplateForm(forms.ModelForm):
    template_file = forms.FileField(required=False, allow_empty_file=True)
    content = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Template
        fields = ['name', 'template_file', 'content']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['content'] and cleaned_data['template_file']:
            raise forms.ValidationError('You can not specify a text and upload a file.')
        elif not cleaned_data['content'] and not cleaned_data['template_file']:
            raise forms.ValidationError('Please specify a text or upload a file.')
        elif cleaned_data['content']:
            cleaned_data['template_file'] = ContentFile(
                cleaned_data.pop('content'),
                name=slugify(cleaned_data['name']))
        else:
            cleaned_data.pop('content')
        return cleaned_data
