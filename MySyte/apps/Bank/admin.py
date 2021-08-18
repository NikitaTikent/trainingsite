from django.contrib import admin
from . import models


admin.site.register(models.User)
admin.site.register(models.Details)
admin.site.register(models.Cars)
