from django.apps import AppConfig

class PapersConfig(AppConfig):
    name = 'papers'
    # this is because the app label papers conflicts with something else
    label = 'papers-app'

