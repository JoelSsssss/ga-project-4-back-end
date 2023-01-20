from .common import TemplatesSerializer
from usercards.serializers import UserCardsSerializer


class PopulatedTemplatesSerializer(TemplatesSerializer):

    usercards = UserCardsSerializer(many=True)
