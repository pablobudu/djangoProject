from django.apps import AppConfig


class WaffledecksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'WaffleDecks'

    def ready(self):
        import WaffleDecks.signals
