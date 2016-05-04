from django.contrib import admin
from .models import Empresa
from .forms import EmpresaForm


class EmpresaAdmin(admin.ModelAdmin):
    form = EmpresaForm

admin.site.register(Empresa, EmpresaAdmin)
