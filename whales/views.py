
# # Create your views here.
#from django.contrib.auth.models import User
from rest_framework import generics


from whales.models import Whale
from .serializers import WhalesSerializer


# Create your views here.
# view created with Generic Views from django library queryset and serializer_class must be used
class WhaleList(generics.ListCreateAPIView):
    queryset = Whale.objects.all()
    serializer_class = WhalesSerializer

 # view created with Generic Views from django library


class WhaleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Whale.objects.all()
    serializer_class = WhalesSerializer

# class WhaleView(APIView):
#     def get(self, _request):
#         whales = Whale.objects.all()
#         serialized_whales = WhalesSerializer(whales, many=True)
#         return Response(serialized_whales.data)


# def post(self, request, format=None):
#     serializer = WhalesSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class WhaleDetailView(APIView):

#     def get(self, _request, pk):
#         whale = Whale.objects.get(id=pk)
#         serialized_whales = WhalesSerializer(whale, many=False)
#         return Response(serialized_whales.data)
