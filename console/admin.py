from django.contrib import admin
from .models import Certificate, VendorVPN, Application

# Register your models here.

# Registrar os modelos papra o painel de administração do Django (sem personalizações)
admin.site.register(Certificate)
admin.site.register(VendorVPN)
admin.site.register(Application)