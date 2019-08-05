from django.contrib import admin

from .forms import TemplateForm
from .models import Template


class TemplateAdmin(admin.ModelAdmin):
    form = TemplateForm
    list_display = ('name', 'format', 'linked_object', 'added', 'updated')


admin.site.register(Template, TemplateAdmin)
