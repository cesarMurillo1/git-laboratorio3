from django.apps import AppConfig


class AgendawebConfig(AppConfig):
    name = 'AgendaWeb'
    def ready(self):
        import AgendaWeb.signals