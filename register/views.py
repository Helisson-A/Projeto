from django.shortcuts import render
from rest_framework import response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from register.api.serializers import registerSerializer

class CadstroAPIView(APIView):

    def post(self, request):
        serializer = registerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def registerPost(request):
    serializer = registerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return response(serializer.data)
    return response.ResponseHeaders(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
