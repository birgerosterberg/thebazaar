from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from bazaar.models import Product
from .models import Wishlist


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    return redirect('mywishlist')  # Redirect as appropriate


@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist = Wishlist.objects.get(user=request.user)
    wishlist.products.remove(product)
    return redirect('mywishlist')  # Redirect as appropriate


@login_required
def wishlist_view(request):
    try:
        wishlist = Wishlist.objects.get(user=request.user)
        products = wishlist.products.all()
    except Wishlist.DoesNotExist:
        products = []

    return render(request, 'wishlist/wishlist_page.html',
                  {'products': products})
