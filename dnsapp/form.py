from django.forms import ModelForm
from .models import Registro

class RegisterForm(ModelForm):
    class Meta:
        model = Registro
        fields = ['ip','dominio2','categoria','prioridade']