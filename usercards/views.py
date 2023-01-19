from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import UserCards
from .serializers import UserCardsSerializer


class UserCardsListView(APIView):

    def get(self, _request):
        usercards = UserCards.objects.all()
        serialized_products = UserCardsSerializer(usercards, many=True)
        return Response(serialized_products.data, status=status.HTTP_200_OK)
