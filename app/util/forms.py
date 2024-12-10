from datetime import datetime

from crispy_forms import layout
from crispy_forms.helper import FormHelper
from django import forms

from .models import Parametro


class ParametroForm(forms.ModelForm):
    class Meta:
        model = Parametro
        fields = ["valor"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["valor"] = self.get_valor_field()

    @property
    def helper(self):
        helper = FormHelper(self)
        helper.layout = layout.Layout(layout.Row(layout.Column("valor")))
        return helper

    def get_valor_field(self):
        field = {
            Parametro.Tipo.TEXTO: forms.CharField,
            Parametro.Tipo.NUMERO: forms.IntegerField,
            Parametro.Tipo.DECIMAL: forms.FloatField,
            Parametro.Tipo.FECHA: forms.DateField,
            Parametro.Tipo.FECHA_HORA: forms.DateTimeField,
            Parametro.Tipo.BOOLEANO: forms.BooleanField,
        }[self.instance.tipo]

        if self.instance.tipo == Parametro.Tipo.FECHA:
            field.widget = forms.DateInput(attrs={"type": "date"})
        elif self.instance.tipo == Parametro.Tipo.FECHA_HORA:
            field.widget = forms.DateTimeInput(attrs={"type": "datetime-local"})

        return field(label=self.instance.nombre, initial=self.instance.valor)

    def post_valor(self):
        if self.instance.tipo == Parametro.Tipo.FECHA_HORA:
            if len(self.instance.valor.split("-")) > 3:
                y, m, dhms, _ = self.instance.valor.split("-")
                d, hms = dhms.split(" ")
                self.instance.valor = datetime.strptime(f"{y}-{m}-{d} {hms}", "%Y-%m-%d %H:%M:%S")
            else:
                self.instance.valor = datetime.strptime(self.instance.valor, "%Y-%m-%d %H:%M:%S")


class ParametroFormSet(forms.BaseModelFormSet):
    @staticmethod
    def create(data=None, modulo=None):
        formset = forms.modelformset_factory(
            Parametro,
            form=ParametroForm,
            formset=ParametroFormSet,
            extra=0,
            can_delete=False,
        )
        qs = Parametro.objects.filter(modulo__identificador=modulo) if modulo else Parametro.objects.none()
        return formset(data=data, queryset=qs)

    @property
    def get_helper(self):
        helper = FormHelper()
        helper.form_method = "POST"
        return helper
