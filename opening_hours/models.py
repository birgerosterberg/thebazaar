from django.db import models

class OpeningHours(models.Model):
    monday = models.CharField("Monday", max_length=50, blank=True, help_text="Enter time in 24-hour format (e.g., 09:00 - 17:00)")
    tuesday = models.CharField("Tuesday", max_length=50, blank=True, help_text="Enter time in 24-hour format (e.g., 09:00 - 17:00)")
    wednesday = models.CharField("Wednesday", max_length=50, blank=True, help_text="Enter time in 24-hour format (e.g., 09:00 - 17:00)")
    thursday = models.CharField("Thursday", max_length=50, blank=True, help_text="Enter time in 24-hour format (e.g., 09:00 - 17:00)")
    friday = models.CharField("Friday", max_length=50, blank=True, help_text="Enter time in 24-hour format (e.g., 09:00 - 17:00)")
    saturday = models.CharField("Saturday", max_length=50, blank=True, help_text="Enter time in 24-hour format (e.g., 09:00 - 17:00)")
    sunday = models.CharField("Sunday", max_length=50, blank=True, help_text="Enter time in 24-hour format (e.g., 09:00 - 17:00)")

    def __str__(self):
        return "Opening Hours"

    class Meta:
        verbose_name_plural = "Opening Hours"