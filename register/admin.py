from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import Group, User
from .forms import registroChangeForm, registroCreationForm
from .models import registro


@admin.register(registro)
class UserAdmin(auth_admin.UserAdmin):
    form = registroChangeForm
    add_form = registroCreationForm
    Group = Group
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Campos personalizados",
        {"fields": ("DataNascimento", "Celular", "EndRua", "EndNumero", "EndComplemento", "EndBairro", "EndCidade", "NomeInstituicao", "SiteInstituicao", "SobreInstituicao", "bitAtivo", "CheckInstituicao",)}
        ),
    )