from django.db import models


class Template(models.Model):
    name = models.CharField(max_length=256, unique=True)
    template_file = models.FileField(upload_to='template_model')

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
