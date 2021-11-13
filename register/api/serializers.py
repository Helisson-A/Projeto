from rest_framework import serializers

from register import models

class registerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.registro
        fields = '__all__'

