from django.shortcuts import render
from bazaar.models import Product

def index(request):
    # Fetch the top 8 products with the highest rating
    top_products = Product.objects.all().order_by('-rating', '-id')[:12]
    return render(request, 'home/index.html', {'products': top_products})
