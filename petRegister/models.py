from django.db import models

from uuid import uuid4

from Register.models import Registro


def upload_imagem_pet(instance, filename):
    return f"{instance.Pet_ID}-{filename}"

class PetRegistro(models.Model):
        PORTE = (
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande')
        )
        SEXO = (
        ('M', 'Macho'),
        ('F', 'Femea')
        )
        Pet_ID = models.UUIDField(primary_key=True, default=uuid4, editable=False)
        Usuario_ID = models.ForeignKey(Registro, on_delete=models.CASCADE)
        NomePet = models.CharField(max_length=100)
        Idade = models.IntegerField()
        Sexo = models.CharField(max_length=1, choices=SEXO, blank=False, null=False, default='M')
        Porte = models.CharField(max_length=1, choices=PORTE, blank=False, null=False, default='M')
        Imagem = models.ImageField(upload_to=upload_imagem_pet, null=True, blank=True)
        Especie = models.CharField(max_length=100)
        btCastrado = models.BooleanField()
        btVacinado = models.BooleanField()
        btVermifugado = models.BooleanField()
        DescricaoAnimal = models.TextField()
        bitDoador = models.BooleanField()

        def __str__(self):
            return self.NomePet

class MensagemPet(models.Model):
    ID_Pergunta = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    Id_Pet = models.ForeignKey(PetRegistro, on_delete=models.CASCADE)
    Pergunta = models.TextField()
    Resposta = models.TextField()

