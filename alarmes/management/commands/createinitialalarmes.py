from django.core.management.base import BaseCommand, CommandError
from alarmes.models import Alarme
from leituras.models import Leitura
from datetime import datetime, timezone


class Command(BaseCommand):
    help = "Creates initial alarmes."

    def handle(self, *args, **options):
        leituras = Leitura.objects.order_by("data_leitura")[:20]

        for leitura in leituras:
            Alarme.objects.create(
                rgiPrincipal=leitura.rgi_principal,
                rgiAutonoma=leitura.rgi_autonoma,
                codigoAlarme="F1",
                descricaoAlarme="Possivel vazamento",
                dataAlarme=leitura.data_leitura.replace(tzinfo=timezone.utc),
            )
