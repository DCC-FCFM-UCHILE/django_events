# Generated by Django 5.1.4 on 2024-12-10 15:08

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Parametro",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("fecha_creacion", models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creación")),
                ("fecha_modificacion", models.DateTimeField(auto_now=True, verbose_name="Fecha Modificación")),
                ("nombre", models.CharField(blank=True, max_length=100, null=True, verbose_name="Nombre")),
                ("identificador", models.CharField(db_index=True, max_length=250, null=True, verbose_name="Identificador")),
                ("valor", models.CharField(max_length=250, null=True, verbose_name="Valor")),
                (
                    "tipo",
                    models.CharField(
                        choices=[
                            ("texto", "Texto"),
                            ("numero", "Número"),
                            ("decimal", "Decimal"),
                            ("fecha", "Fecha"),
                            ("fecha_hora", "Fecha y Hora"),
                            ("booleano", "Booleano"),
                        ],
                        default="texto",
                        max_length=50,
                        verbose_name="Tipo",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Parámetros",
                "ordering": ("nombre",),
            },
        ),
        migrations.CreateModel(
            name="Texto",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("fecha_creacion", models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creación")),
                ("fecha_modificacion", models.DateTimeField(auto_now=True, verbose_name="Fecha Modificación")),
                ("identificador", models.CharField(max_length=250, null=True, verbose_name="Identificador")),
                ("texto", tinymce.models.HTMLField()),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
