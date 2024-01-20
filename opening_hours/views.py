from datetime import date
from .models import OpeningHours


def get_todays_hours():
    weekdays = ['monday',
                'tuesday',
                'wednesday',
                'thursday',
                'friday',
                'saturday',
                'sunday']
    today = date.today().weekday()
    try:
        hours = OpeningHours.objects.latest('id')
        return getattr(hours, weekdays[today], "Closed")
    except OpeningHours.DoesNotExist:
        return "Closed"


def get_weekly_hours():
    try:
        return OpeningHours.objects.latest('id')
    except OpeningHours.DoesNotExist:
        return None
