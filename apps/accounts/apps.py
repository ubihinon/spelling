from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'apps.accounts'
    label = 'apps_accounts'

    def ready(self):
        import apps.accounts.receivers
