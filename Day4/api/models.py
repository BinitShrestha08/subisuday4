from django.db import models

# Create your models here.

class OLT(models.Model):
    timestamp = models.CharField(max_length=100)
    hostname= models.CharField(max_length=100)
    phyinterface = models.CharField(max_length=100)
    serialnumber = models.CharField(max_length=50)

    class meta:
        unique_togther = ('hostname', 'phyinterface', 'serialnumber')