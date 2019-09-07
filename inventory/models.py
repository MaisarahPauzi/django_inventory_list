from django.db import models

# Create your models here.
class Devices(models.Model):
    types = models.CharField(max_length=100, blank=False)
    price = models.IntegerField()

    choices = (
        ('AVAILABLE','Item ready to purchase'),
        ('SOLD','Item sold'),
        ('RESTOCKING','Item restocking in few days')
    )

    status = models.CharField(max_length=100, choices=choices, default="SOLD")
    issues = models.CharField(max_length=100, default="No issues")

    def __str__(self):
        return 'Type : {0} Price : {1}'.format(self.types, self.price)

class Laptop(Devices):
    pass

class Desktop(Devices):
    pass

class Mobile(Devices):
    pass

