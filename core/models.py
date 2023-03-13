from django.db import models
import uuid

# Create your models here.
class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(blank=True)
    description = models.CharField(max_length=100, blank=True)
    amount = models.IntegerField(blank=True)
    mode = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.description
