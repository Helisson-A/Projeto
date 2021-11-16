from django.db.models.query import QuerySet
from rest_framework import generics, serializers, viewsets
from petRegister.api.serializers import ListaPetSerializer, PetSerializer, PetMensagementSerializer, ListaMensagemSerializer
from petRegister import models

class PetViewSet(viewsets.ModelViewSet):
    serializer_class = PetSerializer
    queryset = models.PetRegistro.objects.all()

class PetMensagemViewSet(viewsets.ModelViewSet):
    serializer_class = PetMensagementSerializer
    queryset = models.MensagemPet.objects.all()

class ListaMensagem(generics.ListAPIView):
    def get_queryset(self):
        queryset = models.MensagemPet.objects.filter(Id_Pet=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMensagemSerializer

class ListaPet(generics.ListAPIView):
    def get_queryset(self):
        queryset = models.PetRegistro.objects.filter(id_cadastro=self.kwargs['pk'])
        return queryset
    serializer_class = ListaPetSerializer