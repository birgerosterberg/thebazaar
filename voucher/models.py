from django.db import models

class Voucher(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.code} - {self.discount_percentage}%"