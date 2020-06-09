from django.template.base import Origin
from django.template.exceptions import TemplateDoesNotExist
from django.template.loaders.base import Loader as BaseLoader

from template_model.models import Template


class Loader(BaseLoader):
    """
    A custom template loader to load templates from the database.

    Tries to load the template from the dbtemplates cache backend specified
    by the DBTEMPLATES_CACHE_BACKEND setting. If it does not find a template
    it falls back to query the database field ``name`` with the template path
    and ``sites`` with the current site.
    """
    is_usable = True

    def get_template_sources(self, template_name):
        yield Origin(
            name=template_name,
            template_name=template_name,
            loader=self,
        )

    def get_contents(self, origin):
        try:
            template = Template.objects.get(template_file=origin.template_name)
            with template.template_file.open() as my_template:
                try:
                    return my_template.read().decode()
                except UnicodeDecodeError:
                    return my_template.read()

        except Template.DoesNotExist:
            raise TemplateDoesNotExist(origin.template_name)
