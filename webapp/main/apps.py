from django.apps import AppConfig
import sys

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        chosen_command = sys.argv[1]
