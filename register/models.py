from django.contrib.auth.models import AbstractUser
from django.db import models

class registro(AbstractUser):
    DataNascimento = models.DateField(null=True)
    Celular = models.CharField(max_length=100, null=True)
    EndRua = models.IntegerField(blank=True, null=True)
    EndNumero = models.IntegerField(blank=True, null=True)
    EndComplemento = models.CharField(max_length=255, blank=True, null=True)
    EndBairro = models.CharField(max_length=255, blank=True, null=True)
    EndCidade = models.CharField(max_length=100, blank=True, null=True)
    NomeInstituicao = models.CharField(max_length=100, blank=True, null=True)
    SiteInstituicao = models.CharField(max_length=100, blank=True, null=True)
    SobreInstituicao = models.CharField(max_length=255, blank=True, null=True)
    bitAtivo = models.BooleanField(default=True, null=True)
    CheckInstituicao = models.BooleanField(default=False, null=True)
