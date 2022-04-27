from django.db import models

# Create your models here. 
def f(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        return '{}.{}'.format(instance.pk, ext)
    else:
        pass

def update_filename(instance, filename):
        path = "media/file/"
        format = instance.id + instance.uuid + instance.file_extension
        return os.path.join(path, format)

class FileName(models.Model):
    title = models.CharField(max_length=50)
    files = models.FileField(upload_to=update_filename, max_length=255, default=None, null=True)