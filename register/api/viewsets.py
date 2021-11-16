from django.http import response
from rest_framework import serializers, viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from register.api.serializers import registerSerializer
from register import models

class registerViewSet(viewsets.ModelViewSet):
    serializer_class = registerSerializer
    queryset = models.registro.objects.all()
    permission_classes = []





