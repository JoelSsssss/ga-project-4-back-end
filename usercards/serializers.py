from rest_framework import serializers
from .models import UserCards
from comments.serializers.common import PopulatedCommentSerializer
from templates.serializers.common import TemplatesSerializer
from jwt_auth.serializers.common import UserSerializer


class UserCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCards
        fields = '__all__'


class PopulatedUserCardsSerializer(UserCardsSerializer):
    templates = TemplatesSerializer(many=True)
    comments = PopulatedCommentSerializer(many=True)
    owner = UserSerializer()
