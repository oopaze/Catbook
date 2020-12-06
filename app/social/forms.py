from django import forms
from tabelas.models import Publicacao

class PublicacaoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['text'].widget.attrs['class'] = 'form-control bg-dark'
        self.fields['text'].widget.attrs['placeholder'] = 'O que seu bixinho está pensando?'
        

    class Meta:
        model = Publicacao
        fields = ('text', 'image')
