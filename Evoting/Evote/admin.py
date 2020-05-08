from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.Parliamentvoting)
admin.site.register(models.Lagislative_voting)
