
from shortlink.rules.stack import SHORTLINK_RULESTACK
from gpm.interfaces.validators import InterfaceValidators
from django import forms

class CreateForm(forms.Form):
    """Recept the new user info."""
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

class GetForm(forms.Form):
    """Recept the new user info."""
    class Meta:
        fields = [
            '_in'
        ]

    _in = InterfaceValidators(
        stack=SHORTLINK_RULESTACK,
        required=True
    )

    _custom = forms.CharField(
        required=False,
    )