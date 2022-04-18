
# Create your views here.
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from whales.models import Whale
from .serializers import WhalesSerializer


# Create your views here.


class WhaleView(APIView):

    def get(self, _request):
        whales = Whale.objects.all()
        serialized_whales = WhalesSerializer(whales, many=True)
        return Response(serialized_whales.data)


class WhaleDetailView(APIView):

    def get(self, _request, pk):
        whale = Whale.objects.get(id=pk)
        serialized_whales = WhalesSerializer(whale, many=False)
        return Response(serialized_whales.data)
