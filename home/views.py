from django.shortcuts import render
from bazaar.models import Product
from opening_hours.views import get_todays_hours, get_weekly_hours

def index(request):
    products = Product.objects.all().order_by('-rating')[:12]
    today_hours = get_todays_hours()
    weekly_hours = get_weekly_hours()

    context = {
        'products': products,
        'today_hours': today_hours,
        'weekly_hours': weekly_hours
    }
    return render(request, 'home/index.html', context)
