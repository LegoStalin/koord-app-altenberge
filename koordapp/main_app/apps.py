from django.apps import AppConfig
import importlib
# from django.contrib.auth.models import Group


class LogsystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_app'
    def ready(self):

        # Erstellung der Rechte Gruppen
        try:
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
            pass
        # Erstelle verschiedene AGKategorien 
        try:
            models = importlib.import_module('main_app.models')
            if not models.AGKategorie.objects.filter(name='Sport').exists():
                models.AGKategorie.objects.create(name='Sport')
            if not models.AGKategorie.objects.filter(name='Lernen').exists():
                models.AGKategorie.objects.create(name='Lernen')
            if not models.AGKategorie.objects.filter(name='Kreativ').exists():
                models.AGKategorie.objects.create(name='Kreativ')
        except:
            pass
