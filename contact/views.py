from django.shortcuts import render
from opening_hours.views import get_weekly_hours


def contact(request):
    # Call the function to get weekly hours
    weekly_hours = get_weekly_hours()
    context = {
        # Add the weekly hours to the context
        'weekly_hours': weekly_hours
    }
    return render(request, 'contact/contact.html', context)
