from django.db import models


# Create your models here.
class Phone(models.Model):
    name = models.CharField(max_length=30)
    mark = models.CharField(max_length=30)
    year = models.IntegerField()
    price_usd = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.mark} | {self.year} | {self.price_usd}$'
