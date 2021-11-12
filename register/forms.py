from django.contrib.auth import forms

from .models import registro

class registroChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = registro

class registroCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = registro