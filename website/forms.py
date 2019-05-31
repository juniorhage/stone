from desafiostone.models import Funcionario
from django import forms


# FORMULÁRIO DE INCLUSÃO DE FUNCIONÁRIOS
# -------------------------------------------

class InsereFuncionarioForm(forms.ModelForm):

    class Meta:
        # Modelo base
        model = Funcionario

        # Campos que estarão no form
        fields = [
            'nome',
            'idade',
            'cargo'
        ]