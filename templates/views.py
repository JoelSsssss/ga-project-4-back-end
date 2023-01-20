from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers.populated import PopulatedTemplatesSerializer
from .models import Templates


class TemplatesListView(APIView):

    def get(self, _request):
        templates = Templates.objects.all()
        serialized_templates = PopulatedTemplatesSerializer(
            templates, many=True)
        return Response(serialized_templates.data, status=status.HTTP_200_OK)
