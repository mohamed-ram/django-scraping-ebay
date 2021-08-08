from django.db import models
from .constants import Department, Brand


class WatchSearch(models.Model):
    department = models.CharField(max_length=20, choices=Department.choices)
    brand = models.CharField(max_length=20, choices=Brand.choices)
    price_from = models.DecimalField(max_digits=8, decimal_places=2)
    price_to = models.DecimalField(max_digits=8, decimal_places=2)


