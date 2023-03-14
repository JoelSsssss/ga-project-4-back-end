from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from rest_framework.exceptions import NotFound

from .models import UserCards
from .serializers import UserCardsSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class UserCardsListView(APIView):
    # permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, _request):
        usercards = UserCards.objects.all()
        serialized_products = UserCardsSerializer(usercards, many=True)
        return Response(serialized_products.data, status=status.HTTP_200_OK)

    def post(self, request):
        # <- this is the line we need to add
        request.data['owner'] = request.user.id
        print(request.data)
        usercards_to_add = UserCardsSerializer(data=request.data)
        try:
            usercards_to_add.is_valid()
            usercards_to_add.save()
            return Response(usercards_to_add.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            res = {
                "detail": str(e)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail": "Unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class UserCardsDetailView(APIView):

    def get(self, _request, pk):
        try:
            usercards = UserCards.objects.get(pk=pk)
            serialized_usercards = UserCardsSerializer(usercards)
            return Response(serialized_usercards.data, status=status.HTTP_200_OK)
        except UserCards.DoesNotExist:
            raise NotFound(detail="Can't find that user card!")

    def get_usercards(self, pk):
        try:
            return UserCards.objects.get(pk=pk)
        except UserCards.DoesNotExist:
            raise NotFound(detail="🆘 Can't find that user card!")

    def get(self, _request, pk):
        usercards = self.get_usercards(pk=pk)
        serialized_usercards = UserCardsSerializer(usercards)
        return Response(serialized_usercards.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        usercards_to_edit = self.get_usercards(pk=pk)
        updated_usercards = UserCardsSerializer(
            usercards_to_edit, data=request.data)
        try:
            updated_usercards.is_valid()
            updated_usercards.save()
            return Response(updated_usercards.data, status=status.HTTP_202_ACCEPTED)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            res = {
                "detail": "Unprocessable Entity"
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        usercards_to_delete = self.get_usercards(pk=pk)
        usercards_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
