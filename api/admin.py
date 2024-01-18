from django.contrib import admin
from .models import User, TravelPlan, Booking

# Register your models here.
admin.site.register(User)
admin.site.register(TravelPlan)
admin.site.register(Booking)
