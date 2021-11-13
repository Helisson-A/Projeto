from rest_framework import viewsets
from register.api.serializers import registerSerializer
from register import models

class registerViewSet(viewsets.ModelViewSet):
    serializer_class = registerSerializer
    queryset = models.registro.objects.all()

