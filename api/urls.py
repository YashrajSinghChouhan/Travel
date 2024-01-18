from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index),
    path('getUser/',views.getUser),
    path('getTravelPlan/',views.getTravelPlan),
    path('getBooking/',views.getBooking),
]