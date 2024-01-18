from rest_framework.serializers import ModelSerializer
from .models import User, TravelPlan, Booking

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TravelPlanSerializer(ModelSerializer):
    class Meta:
        model = TravelPlan
        fields = '__all__'

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'