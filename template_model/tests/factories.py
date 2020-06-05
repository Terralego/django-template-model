import factory
import os
from template_model.models import Template


class TemplateHTMLFactory(factory.DjangoModelFactory):
    name = "HTML template"
    template_file = factory.django.FileField(from_path=os.path.join(os.path.dirname(__file__), "test.html"))

    class Meta:
        model = Template
