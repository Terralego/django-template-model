from django.contrib import admin

from .models import Template
from .forms import TemplateForm


class TemplateAdmin(admin.ModelAdmin):
    form = TemplateForm
    list_display = ('name', 'added', 'updated')
    readonly_fields = ('template_file',)

    def get_readonly_fields(self, request, obj=None):
        # Allows to specify the template file at creation, but disable it on change forms.
        if obj:
            return self.readonly_fields
        else:
            return []

admin.site.register(Template, TemplateAdmin)
