from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Booking, TravelPlan
from .serializer import UserSerializer, TravelPlanSerializer, BookingSerializer

# Create your views here.
def index(request):
    return HttpResponse("Hello world")

@api_view(['GET'])
def getUser(request):
    data = User.objects.all()
    return Response(UserSerializer(data,many=True).data)

@api_view(['GET'])
def getTravelPlan(request):
    data = TravelPlan.objects.all()
    return Response(TravelPlanSerializer(data,many=True).data)

@api_view(['GET'])
def getBooking(request):
    data = Booking.objects.all()
    return Response(BookingSerializer(data,many=True).data)