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
    SWATCH = "SWATCH", "Swatch"
    CASIO = "CASIO", "Casio"
    BALL = "BALL", "Ball"
    BREITLING = "BREITLING", "Breitling"
    HAMILTON = "HAMILTON", "Hamilton"
    TISSOT = "TISSOT", "Tissot"

