from django.views.generic import ListView
from .models import Curso


class CursoListView(ListView):
    model = Curso
    template_name = "curso_list_html"
