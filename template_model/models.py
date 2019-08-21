from django.db import models


FORMAT_CHOICES = (
    ('odt', 'odt'),
    ('html', 'html'),
    ('docx', 'docx'),
)


class Template(models.Model):
    name = models.CharField(max_length=256, unique=True)
    format = models.CharField(max_length=256, choices=FORMAT_CHOICES)
    content = models.TextField()

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
