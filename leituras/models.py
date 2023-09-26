import os
import uuid
from django.db import models

from django.contrib.auth.models import User


# XXX - internal
def sheet_upload_to(instance, filename):
    # Get the ID of the Post instance
    sheet_id = instance.leitura.id

    # Construct the file path using the ID and filename
    return os.path.join("uploads/leituras", str(sheet_id), filename)


class Relatorio(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    class Meta:
        verbose_name_plural = "Relatórios"
        ordering = ["created_at"]

    # XXX - internal
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.created_at.strftime("%d/%m/%Y %H:%M")


class Folha(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    relatorio = models.ForeignKey(
        Relatorio, on_delete=models.CASCADE, related_name="folhas"
    )
    arquivo = models.FileField(upload_to="uploads/%Y/%m/%d/")

    # XXX - internal
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.arquivo.name.split("/")[-1]


# @pghistory.track(pghistory.Snapshot())
class Leitura(models.Model):
    class Meta:
        ordering = ["data_leitura"]

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    folha = models.ForeignKey(Folha, on_delete=models.CASCADE)

    rgi_principal = models.CharField(max_length=100)
    rgi_autonoma = models.CharField(max_length=100)
    status_valvula = models.CharField(max_length=100)
    data_leitura = models.DateTimeField()
    leitura = models.IntegerField()
    fria_quente = models.CharField(max_length=100)
    imovel = models.CharField(max_length=100)
    hidrometro = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} - {self.rgi_principal} - {self.rgi_autonoma} - {self.data_leitura}"


class RelatorioEvento(models.Model):
    class EventTypes(models.TextChoices):
        CRIADO = "criado"
        ATUALIZADO = "atualizado"
        DELETADO = "deletado"

    relatorio = models.ForeignKey(
        Relatorio, on_delete=models.CASCADE, related_name="eventos"
    )
    funcionario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="funcionarios"
    )
    event_date = models.DateTimeField(auto_now_add=True)
    event_type = models.CharField(
        max_length=100, choices=EventTypes.choices, default=EventTypes.CRIADO
    )
