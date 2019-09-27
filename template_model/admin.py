from django.contrib import admin

from .models import Template
from .forms import TemplateForm


class TemplateAdmin(admin.ModelAdmin):
    form = TemplateForm
    list_display = ('name', 'created_at', 'updated_at')


admin.site.register(Template, TemplateAdmin)
