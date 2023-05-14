from django.apps import AppConfig
from ditto.ai_models.main_controlnet import MainControlNet


class DittoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ditto'
    model = MainControlNet()
    
    # def ready(self):
    #     from ditto.jobs import updater
    #     updater.start()
