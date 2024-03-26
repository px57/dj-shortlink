from django.db import models
from django.forms.models import model_to_dict

from gpm.models.base_metadata_model import BaseMetadataModel

from shortlink.rules.stack import SHORTLINK_RULESTACK

class ShortLink(BaseMetadataModel):
    """
    ShortLink model
    """
    profile = models.ForeignKey(
        'profiles.Profile', 
        on_delete=models.CASCADE, 
        related_name='short_links',
        null=True,
        blank=True,
    )

    interface = models.CharField(
        max_length=255, 
        default='DEFAULT', 
        choices=SHORTLINK_RULESTACK.models_choices()
    )

    short_link = models.CharField(
        max_length=255, 
        unique=True
    )

    original_link = models.CharField(
        max_length=255, 
        unique=True
    )

    class Meta:
        db_table = 'short_link'
        verbose_name = 'Short Link'
        verbose_name_plural = 'Short Links'

    def __str__(self):
        return self.short_link

    def serialize(self, request):
        """
        Serialize the shortlink.
        """
        serialize = model_to_dict(self)
        return serialize