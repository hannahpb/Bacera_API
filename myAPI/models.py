from unicodedata import name
from django.db import models

# Create your models here.

class vehicls(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=100)

    def _str_(self):
        return self.name