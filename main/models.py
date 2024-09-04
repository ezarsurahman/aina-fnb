from django.db import models

class FoodEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    ready = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    @property
    def is_pricy(self):
        return self.price > 50000
