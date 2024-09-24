from django.db import models
from django.contrib.auth.models import User
import uuid

class FoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    img = models.CharField(max_length=1000)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    ready = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    @property
    def is_pricy(self):
        return self.price > 50000
