from django.db import models
from magic import from_buffer


class Template(models.Model):
    name = models.CharField(max_length=256, unique=True)
    mime_type = models.CharField(max_length=256)
    template_file = models.FileField()

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.mime_type})"

    def save(self, *args, **kwargs):
        self.mime_type = from_buffer(self.template_file.read(), mime=True)
        super().save(*args, **kwargs)
