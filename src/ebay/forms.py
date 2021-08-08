from django import forms
from django.db import models

from .models import WatchSearch


class WatchSearchForm(forms.ModelForm):
    class Meta:
        model = WatchSearch
        fields = "__all__"

