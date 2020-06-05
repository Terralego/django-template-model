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

    def get_template_sources(self, template_name, template_dirs=None):
        yield Origin(
            name=template_name,
            template_name=template_name,
            loader=self,
        )

    def get_contents(self, origin):
        return self._load_template_source(origin.template_name)

    def _load__template(self, template_name):
        template = Template.objects.get(template_file=template_name)
        with template.template_file.open('rb+') as my_template:
            return my_template.read()

    def _load_template_source(self, template_name, template_dirs=None):
        try:
            return self._load__template(template_name)
        except Template.DoesNotExist:
            TemplateDoesNotExist(template_name)
