from rest_framework import serializers
from .models import UserCards
from comments.serializers.common import CommentSerializer
from templates.serializers.common import TemplatesSerializer


class UserCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCards
        fields = '__all__'


class PopulatedUserCardsSerializer(UserCardsSerializer):
    templates = TemplatesSerializer(many=True)
    comments = CommentSerializer(many=True)
