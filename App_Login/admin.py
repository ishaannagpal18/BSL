from django.contrib import admin
from .models import *
from import_export.admin import ExportActionMixin
# Register your models here.
# admin.site.register(Register)

class RegisterAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'email_id', 'contact_no')

admin.site.register(Register, RegisterAdmin)