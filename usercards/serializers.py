from rest_framework import serializers
from .models import UserCards


class UserCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCards
        fields = '__all__'
