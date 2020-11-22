from django.db import models

# Create your models here.
class Cars(models.Model):
    name = models.CharField(max_length=200,null=True,blank=False)
    model = models.CharField(max_length=200)
    price = models.FloatField(max_length=200)
    mileage = models.FloatField(max_length=200)
    power = models.IntegerField(null=True)
    seat_num = models.IntegerField(null=True)

    def __str__(self):
        return self.name
