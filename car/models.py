from django.db import models


class Cars(models.Model):
    name = models.CharField(max_length=200, null=True, blank=False)
    fuel = models.CharField(max_length=200, null=True)
    tank_capacity = models.IntegerField(null=True)
    price = models.FloatField(max_length=200)
    engine_capacity = models.FloatField(max_length=200)
    power = models.IntegerField(null=True)
    ground_clearance = models.IntegerField(null=True)
    description = models.TextField(max_length=1500, null=True)
    extras = models.TextField(max_length=1500, null=True)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True, blank=False)
    phone = models.CharField(max_length=200, null=True)
    message = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.name) if self.name else ""


class Book(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    date_booked = models.DateTimeField(auto_now_add=True)
    carname = models.CharField(max_length=200, blank=True, null=True)
    complete = models.BooleanField(max_length=200, null=True)

    def __str__(self):
        return str(f"{self.customer.name} book")