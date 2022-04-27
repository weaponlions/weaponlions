from django.contrib import admin
from .models import FileName
# Register your models here.
@admin.register(FileName)
class FileNameAdmin(admin.ModelAdmin):
    list_display = ('title', 'files')
