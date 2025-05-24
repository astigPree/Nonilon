from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.ProgrammingLanguage)
admin.site.register(models.OtherLanguage)
admin.site.register(models.UsedFrameWork)
admin.site.register(models.UsedLibrary)
admin.site.register(models.UsedSoftware)

admin.site.register(models.SoftwareProject)
admin.site.register(models.HardwareProject)

admin.site.register(models.Client)