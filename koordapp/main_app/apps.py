from django.apps import AppConfig
import importlib
# from django.contrib.auth.models import Group


class LogsystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_app'
    def ready(self):
        try:
            # Erstellung der Rechte Gruppen
            models = importlib.import_module('django.contrib.auth.models')
            if not models.Group.objects.filter(name='Admin').exists():
                models.Group.objects.create(name='Admin')
            if not models.Group.objects.filter(name='Gruppenleitung').exists():
                models.Group.objects.create(name='Gruppenleitung')
            if not models.Group.objects.filter(name='Raumbetreuer').exists():
                models.Group.objects.create(name='Raumbetreuer')
            if not models.Group.objects.filter(name='Ohne Rolle').exists():
                models.Group.objects.create(name='Ohne Rolle')
        except:
            print('')