from django.db import models
from django.contrib.auth.models import User
import uuid

class FoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    img = models.CharField(max_length=1000, verbose_name="Menu Image")
    name = models.CharField(max_length=255, verbose_name="Name")
    price = models.IntegerField(verbose_name="Price (Rp.)")
    ready = models.CharField(max_length=255, verbose_name="Ready?")
    description = models.CharField(max_length=255, verbose_name="Description")

    @property
    def is_pricy(self):
        return self.price > 50000
