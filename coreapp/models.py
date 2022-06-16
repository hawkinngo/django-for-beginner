from django.db import models


class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    is_true = models.BooleanField()

    def __str__(self):
        return self.name
