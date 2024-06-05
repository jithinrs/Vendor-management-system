from django.apps import AppConfig


class VendorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vendors'

    def ready(self):
        from . import signals  # Import the signal handlers


# class MyappConfig(AppConfig):
#     name = 'vendors'

#     def ready(self):
#         from . import signals  # Import the signal handlers
