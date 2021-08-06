from django.apps import AppConfig


class DmcaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dmca'

    def ready(self):
        from .scheduler import scheduler
        scheduler.start()
