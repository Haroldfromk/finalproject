from django.db import models

class dogcharacter(models.Model):
    idx = models.IntegerField(null=True)
    name = models.CharField(max_length=50)
    char = models.TextField(null=True)
    speci = models.TextField(null=True)
