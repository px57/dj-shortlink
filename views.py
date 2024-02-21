from django.shortcuts import render
from kernel.http import Response

from shortlink.__libs__.generate import generate_shortlink
from shortlink.__libs__.redirect import redirect_shortlink

from shortlink.rules.stack import SHORTCUT_RULESTACK

from shortlink import forms

def create(request):
    """
    Create a shortlink.
    """
    res = Response(request=request)
    form = forms.CreateForm(request.POST)
    if not form.is_valid():
        return res.form_error(form)
    data = form.cleaned_data

    print (data)
    return res.success()

def redirect(request, path):
    """
    Redirect to the url.
    """
    res  = Response(request)
    form = forms.RedirectForm(request.POST)
    if not form.is_valid():
        return res.form_error(form)
    data = form.cleaned_data

    print (data)
    return res.success()

def get(request):
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