from rest_framework import serializers
from .models import guest

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = guest
        fields = '__all__'