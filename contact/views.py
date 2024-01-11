from django.shortcuts import render
from opening_hours.views import get_weekly_hours

def contact(request):
    weekly_hours = get_weekly_hours()  # Call the function to get weekly hours
    context = {
        'weekly_hours': weekly_hours  # Add the weekly hours to the context
    }
    return render(request, 'contact/contact.html', context)
