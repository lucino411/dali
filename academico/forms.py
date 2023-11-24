from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    """Form definition for Curso."""

    class Meta:
        """Meta definition for Cursoform."""
        model = Curso
        fields = '__all__'
    

class CursoUpdateForm(forms.ModelForm):
    class Meta:
        model = Curso
        exclude = ['codigo']  # Excluye el campo 'codigo' del formulario
