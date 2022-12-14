from django.forms import ModelForm
from .models import Comentario
from django.forms.widgets import TextInput, EmailInput, Textarea
 
 
class FormComentario(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Para tirar : depois do nome
 
    def clean(self):
        data = self.cleaned_data
        nome = data.get('nome_comentario')
        email = data.get('email_comentario')
        comentario = data.get('comentario')
 
        if len(nome) < 5:
            self.add_error(
                'nome_comentario',
                'Nome precisa ter mais que 5 caracteres.'
            )
 
    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario')
        # labels = { # Não precisa por conta do verbose
        #     'nome': 'Nome',
        #     'descricao': 'Descrição',
        # }
        widgets = {
            'nome_comentario': TextInput(attrs={
                'placeholder': 'Digite seu nome',
                'class': 'form-control',
            }),
            'email_comentario': EmailInput(attrs={
                'placeholder': 'Digite seu e-mail',
                'class': 'form-control',
            }),
            'comentario': Textarea(attrs={
                'placeholder': 'Digite seu cometário',
                'class': 'form-control',
                # 'rows': 5,
            }),
        }