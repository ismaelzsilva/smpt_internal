from django.db import models

# Create your models here.

class FabricationOrders(models.Model):
    fabrication_order = models.IntegerField()
    reference = models.CharField(max_length=50)
    article = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    quantity = models.IntegerField()