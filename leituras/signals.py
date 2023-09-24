from django.db.models.signals import post_save
from django.dispatch import receiver
from leituras.models import Folha


@receiver(post_save, sender=Folha)
def leitura_registrada(sender, **kwargs):
    instance = kwargs.get("instance")
    print(instance)
