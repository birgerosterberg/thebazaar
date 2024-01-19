from django.shortcuts import render
from bazaar.models import Product
from opening_hours.views import get_todays_hours, get_weekly_hours
from blog.models import BlogPost


def index(request):
    products = Product.objects.all().order_by('?')[:20]
    today_hours = get_todays_hours()
    weekly_hours = get_weekly_hours()
    latest_post = BlogPost.objects.all().order_by('-published_date').first()


    context = {
        'products': products,
        'today_hours': today_hours,
        'weekly_hours': weekly_hours,
        'latest_post': latest_post,
    }
    return render(request, 'home/index.html', context)
