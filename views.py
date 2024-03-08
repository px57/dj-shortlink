from django.shortcuts import render

from kernel.http import Response
from kernel.http import load_response
from kernel.http.decorators import load_json

from shortlink.__libs__.generate import generate_shortlink
from shortlink.__libs__.redirect import redirect_shortlink

from shortlink.rules.stack import SHORTLINK_RULESTACK

from shortlink import forms

@load_response(
    stack=SHORTLINK_RULESTACK,
    form=forms.CreateForm,
    json=True,
    load_params=True
)
def create(request, res=None):
    """
    Create a shortlink.
    """
    _in = res.get_interface()
    return res.success()

@load_response(stack=SHORTLINK_RULESTACK)
def redirect(request, path, res=None):
    """
    Redirect to the url.
    """
    _in = res.get_interface()
    form = forms.RedirectForm(request.POST)
    if not form.is_valid():
        return res.form_error(form)
    data = form.cleaned_data

    print (data)
    return res.success()

@load_response(stack=SHORTLINK_RULESTACK)
def get(request, res=None):
    """
    Get the shortlink.

    Args:
        request: the request object.
    """
    res = Response(request=request)
    form = forms.GetForm(request.POST)
    if not form.is_valid():
        return res.form_error(form)
    data = form.cleaned_data

    print (data)
    return res.success()