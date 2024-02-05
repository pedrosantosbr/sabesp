from django.db import models


class Alarme(models.Model):
    class Meta:
        db_table = "alarmes"
        ordering = ["-dataAlarme"]

    rgiPrincipal = models.CharField(max_length=255)
    rgiAutonoma = models.CharField(max_length=255)
    codigoAlarme = models.CharField(max_length=255)
    descricaoAlarme = models.CharField(max_length=255)
    dataAlarme = models.DateTimeField()
