from django.db import models
from django.contrib.auth.models import User

class TransactionLog(models.Model):
    price = models.DecimalField(max_digits=14, decimal_places=5)
    description = models.TextField()
    vendor = models.ForeignKey(User, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.description