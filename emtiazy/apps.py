from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EmtiazyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'emtiazy'
    verbose_name = _("Emtiazy Main Apps")
