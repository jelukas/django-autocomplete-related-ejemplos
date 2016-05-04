from dal import autocomplete
from .models import Empresa
from django import forms


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ('__all__')
        widgets = {
            'pais': autocomplete.ModelSelect2(url='country-autocomplete'),
            'ciudad': autocomplete.ModelSelect2(url='city-autocomplete', forward=['pais'])
        }
