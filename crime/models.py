from django.db import models
from datetime import datetime

# Create your models here.

class Report(models.Model):
    Name = models.CharField(max_length=50)
    PhoneNumber = models.IntegerField()
    IDNumber = models.IntegerField(null=True)
    CrimeType = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


