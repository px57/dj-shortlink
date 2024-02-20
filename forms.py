
from shortlink.rules.stack import SHORTCUT_RULESTACK
from kernel.interfaces.validators import InterfaceValidators
from django import forms

class CreateForm(forms.Form):
    """Recept the new user info."""
    class Meta:
        fields = [
            '_in',
        ]

    _in = InterfaceValidators(
        stack=SHORTCUT_RULESTACK,
        required=True
    )

    url = forms.URLField(
        required=True
    )

class RedirectForm(forms.Form):
    """Recept the new user info."""
    class Meta:
        fields = [
            'path',
        ]

    path = forms.CharField(
        required=True
    )