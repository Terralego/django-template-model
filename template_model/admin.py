from django.contrib import admin

from .models import Template
from .forms import TemplateForm


class TemplateAdmin(admin.ModelAdmin):
    form = TemplateForm
    list_display = ('name', 'mime_type', 'added', 'updated')


admin.site.register(Template, TemplateAdmin)
