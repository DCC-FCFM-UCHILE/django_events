from django.db import models
from tinymce.models import HTMLField

from common.models import BaseModel


class Texto(BaseModel):
    identificador = models.CharField(max_length=250, blank=False, null=True, verbose_name="Identificador")
    texto = HTMLField()

    def __str__(self):
        return f"{self.modulo.identificador}.{self.identificador}"


class Parametro(BaseModel):
    nombre = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nombre")
    identificador = models.CharField(max_length=250, blank=False, null=True, verbose_name="Identificador", db_index=True)
    valor = models.CharField(max_length=250, blank=False, null=True, verbose_name="Valor")

    class Meta:
        verbose_name_plural = "Parámetros"
        ordering = (
            "nombre",
        )

    class Tipo(models.TextChoices):
        TEXTO = "texto", "Texto"
        NUMERO = "numero", "Número"
        DECIMAL = "decimal", "Decimal"
        FECHA = "fecha", "Fecha"
        FECHA_HORA = "fecha_hora", "Fecha y Hora"
        BOOLEANO = "booleano", "Booleano"

    tipo = models.CharField(max_length=50, choices=Tipo.choices, default=Tipo.TEXTO, verbose_name="Tipo")

    def __str__(self):
        return f"{self.modulo}| {self.identificador}: {self.valor}"
