from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


FORMAT_CHOICES = (
    ('odt', 'odt'),
    ('html', 'html'),
    ('docx', 'docx'),
)


class Template(models.Model):
    name = models.CharField(max_length=256, unique=True)
    format = models.CharField(max_length=256, choices=FORMAT_CHOICES)
    content = models.TextField()

    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField()
    linked_object = GenericForeignKey()

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
