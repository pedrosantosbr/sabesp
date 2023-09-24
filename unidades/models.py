from django.db import models
from django.contrib.auth.models import User


class Unidade(models.Model):
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.endereco


class Funcionario(models.Model):
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)

    # XXX - internal
    user = models.OneToOneField(User, on_delete=models.CASCADE)
