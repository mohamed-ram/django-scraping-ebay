from django import forms
from django.db import models


class Department(models.TextChoices):
    MEN = "MEN", "Men"
    WOMEN = "WOMEN", "Women"
    UNISEX = "UNISEX", "Unisex"
    ADULT = "ADULT", "Adult"
    GIRLS = "GIRLS", "Girls"
    KIDS = "KIDS", "Kids"
    BOYS = "BOYS ", "Boys"
    TEEN = "TEEN", "Teen"


class Brand(models.TextChoices):
    ROLEX = "ROLEX", "Rolex"
    CITIZEN = "CITIZEN", "Citizen"
    OMEGA = "OMEGA", "Omega"
    SWATCH = "SWATCH", "Swatch"
    CASIO = "CASIO", "Casio"


class WatchForm(forms.Form):
    department = forms.ChoiceField(choices=Department.choices)
    brand = forms.ChoiceField(choices=Brand.choices)
    price_from = forms.DecimalField(min_value=1)
    price_to = forms.DecimalField(min_value=1)

