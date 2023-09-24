from django.db import models
import os

from unidades.models import Unidade


# XXX - internal
def sheet_upload_to(instance, filename):
    # Get the ID of the Post instance
    sheet_id = instance.leitura.id

    # Construct the file path using the ID and filename
    return os.path.join("uploads/leituras", str(sheet_id), filename)


# class Leitura(models.Model):
#     class CompetenciaTypes(models.TextChoices):
#         JAN = "JAN", "Janeiro"
#         FEV = "FEV", "Fevereiro"
#         MAR = "MAR", "Março"
#         ABR = "ABR", "Abril"
#         MAI = "MAI", "Maio"
#         JUN = "JUN", "Junho"
#         JUL = "JUL", "Julho"
#         AGO = "AGO", "Agosto"
#         SET = "SET", "Setembro"
#         OUT = "OUT", "Outubro"
#         NOV = "NOV", "Novembro"
#         DEZ = "DEZ", "Dezembro"

#     # XXX - internal
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def folhas(self):
#         return self.sheet_set.first(order_by="-created_at")

#     def __str__(self):
#         return self.name


class Relatorio(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)

    class Meta:
        verbose_name_plural = "Relatórios"

    # XXX - internal
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created_at.strftime("%d/%m/%Y %H:%M")


class Leitura(models.Model):
    relatorio = models.ForeignKey(Relatorio, on_delete=models.CASCADE)

    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)

    rgi_principal = models.CharField(max_length=100)
    rgi_autonoma = models.CharField(max_length=100)
    status_valvula = models.CharField(max_length=100)
    data_leitura = models.DateTimeField()
    leitura = models.IntegerField()
    fria_quente = models.CharField(max_length=100)
    imovel = models.CharField(max_length=100)
    hidrometro = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.unidade} - {self.data}"


class Folha(models.Model):
    arquivo = models.FileField(upload_to="uploads/%Y/%m/%d/")

    # XXX - internal
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.arquivo.name.split("/")[-1]
