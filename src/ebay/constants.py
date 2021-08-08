from django.db import models

class Department(models.TextChoices):
    MEN = "MEN", "Men"
    WOMEN = "WOMEN", "Women"


class Brand(models.TextChoices):
    ROLEX = "ROLEX", "Rolex"
    CITIZEN = "CITIZEN", "Citizen"
    OMEGA = "OMEGA", "Omega"
    SWATCH = "SWATCH", "Swatch"
    # CASIO = "CASIO", "Casio"

