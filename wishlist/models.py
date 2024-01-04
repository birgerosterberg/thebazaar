from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User
from bazaar.models import Product  # Import the Product model from your Bazaar app

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.user.username}'s Wishlist"