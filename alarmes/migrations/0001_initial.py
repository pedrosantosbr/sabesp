# Generated by Django 4.2.3 on 2024-02-05 13:06

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Alarme",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rgiPrincipal", models.CharField(max_length=255)),
                ("rgiAutonoma", models.CharField(max_length=255)),
                ("codigoAlarme", models.CharField(max_length=255)),
                ("descricaoAlarme", models.CharField(max_length=255)),
                ("dataAlarme", models.DateTimeField()),
            ],
        ),
    ]
