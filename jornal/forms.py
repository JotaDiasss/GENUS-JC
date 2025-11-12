# Em jornal/forms.py
from django import forms
from .models import Noticia, Genero

class NoticiaForm(forms.ModelForm):
    generos = forms.ModelMultipleChoiceField(
        queryset=Genero.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Noticia
        fields = ['titulo', 'resumo', 'detalhes', 'reporter', 'generos']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'resumo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'detalhes': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'reporter': forms.TextInput(attrs={'class': 'form-control'}),
        }