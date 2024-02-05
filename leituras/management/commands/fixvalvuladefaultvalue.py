from django.core.management.base import BaseCommand, CommandError
from leituras.models import Leitura


class Command(BaseCommand):
    help = "Updates all Leituras with valvula=None to valvula=FECHADA."

    def handle(self, *args, **options):
        Leitura.objects.update(status_valvula=Leitura.StatusValvula.FECHADA)
