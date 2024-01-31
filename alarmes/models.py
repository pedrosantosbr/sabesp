from django.db import models


class Alarme(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    data = models.DateTimeField()

    class Meta:
        db_table = "alarmes"
        ordering = ["id"]
