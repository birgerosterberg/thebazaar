from django.shortcuts import render,redirect, get_object_or_404
from django.db.models import Avg
from checkout.models import OrderLineItem
from profiles.models import UserProfile
from .models import Review

# Create your views here.
def user_can_review_product(user, product):
    user_profile = UserProfile.objects.get(user=user)
    purchased = OrderLineItem.objects.filter(order__user_profile=user_profile, product=product).exists()
    already_reviewed = Review.objects.filter(user=user, product=product).exists()
    return purchased and not already_reviewed


def update_product_rating(product):
    average_rating = product.reviews.aggregate(Avg('rating'))['rating__avg']
    product.rating = average_rating
    product.save()
