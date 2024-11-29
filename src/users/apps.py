from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    Configuration class for the 'users' Django application.

    Attributes:
        default_auto_field (str): Specifies the default primary key field type to be used for models in the app.
            By default, it is set to 'django.db.models.BigAutoField'.
        name (str): The name of the application. In this case, it is 'users'.
    """
    default_auto_field: str = 'django.db.models.BigAutoField'
    name: str = 'users'
