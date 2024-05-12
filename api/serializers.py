from rest_framework.serializers import ModelSerializer
from .models import *
class TravelPlacesSerializer(ModelSerializer):
    class Meta:
        model= TravelPlace
        fields='__all__'

class TouristSiteSerializer(ModelSerializer):
    class Meta:
        model = TouristSite
        fields = '__all__'


class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'



class AirLineSerializer(ModelSerializer):
    class Meta:
        model = AirLine
        fields = '__all__'