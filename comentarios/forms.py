from django.forms import ModelForm
from .models import Comentario
from django.forms.widgets import TextInput, EmailInput, Textarea
from django.conf import settings
import requests


class FormComentario(ModelForm):
    def clean(self):
        raw_data = self.data
        recaptcha_response = raw_data.get('g-recaptcha-response')
        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': settings.RECAPTCHA_PRIVATE_KEY,
                'response': recaptcha_response
            },
            timeout=10
        )
        recaptcha_result = recaptcha_request.json()

        print(settings.RECAPTCHA_PRIVATE_KEY)
        print(recaptcha_result)
        print(recaptcha_result.get('success'))

        if not recaptcha_result.get('success'):
            self.add_error(
                'comentario',
                'Desculpe Mr. Robot, ocorreu um erro.'
            )

        cleaned_data = self.cleaned_data
        nome = cleaned_data.get('nome_comentario')
        email = cleaned_data.get('email_comentario')
        comentario = cleaned_data.get('comentario')

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
