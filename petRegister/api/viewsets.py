from rest_framework import viewsets
from petRegister.api.serializers import PetSerializer, PetMensagementSerializer
from petRegister import models

class PetViewSet(viewsets.ModelViewSet):
    serializer_class = PetSerializer
    queryset = models.PetRegistro.objects.all()

class PetMensagemViewSet(viewsets.ModelViewSet):
    serializer_class = PetMensagementSerializer
    queryset = models.MensagemPet.objects.all()