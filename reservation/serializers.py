from rest_framework import serializers
from .models import Reservation, Guest, Movie



class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['pk','name','email','phone']
        
        
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
                        