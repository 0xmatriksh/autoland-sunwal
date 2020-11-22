from django.db import models

# Create your models here.
class Cars(models.Model):
    name = models.CharField(max_length=200,null=True,blank=False)
    fuel = models.CharField(max_length=200,null=True)
    tank_capacity = models.IntegerField(null=True)
    price = models.FloatField(max_length=200)
    engine_capacity = models.FloatField(max_length=200)
    power = models.IntegerField(null=True)
    ground_clearance = models.IntegerField(null=True)
    photo = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url