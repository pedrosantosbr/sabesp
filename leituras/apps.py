from django.apps import AppConfig


class LeituraConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "leituras"

    def ready(self):
        import leituras.signals
