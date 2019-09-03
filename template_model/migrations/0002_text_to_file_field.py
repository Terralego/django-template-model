import base64

from django.db import migrations, models
from django.core.files.base import ContentFile
from django.utils.text import slugify


def content_to_file(apps, schema_editor):
    Template = apps.get_model('template_model', 'Template')
    for template in Template.objects.all():
        content = template.content
        template_format = template.format
        if template_format == 'odt':
            b_content = base64.b64decode(content)
            mime_type = 'application/vnd.oasis.opendocument.text'
        elif template_format == 'docx':
            b_content = base64.b64decode(content)
            mime_type = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        else:
            b_content = content.encode('utf-8')
        template.template_file = ContentFile(b_content, name=slugify(template.name))
        template.mime_type = mime_type
        template.save()


class Migration(migrations.Migration):

    initial = False

    dependencies = [
        ('template_model', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            'Template',
            'template_file',
            models.FileField(null=True),
        ),
        migrations.AddField(
            'Template',
            'mime_type',
            models.CharField(max_length=256, null=True),
        ),
        migrations.RunPython(content_to_file),
        migrations.RemoveField(
            'Template',
            'content',
        ),
        migrations.RemoveField(
            'Template',
            'format',
        ),
        migrations.AlterField(
            'Template',
            'template_file',
            models.FileField(),
        ),
        migrations.AlterField(
            'Template',
            'mime_type',
            models.CharField(max_length=256),
        )
    ]
