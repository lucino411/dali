from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Curso
from .forms import CursoForm, CursoUpdateForm
from django.urls import reverse_lazy



class CursoListView(ListView):
    model = Curso
    paginate_by = 5 # Número de elementos por página
    template_name = "curso_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        # iterable = Curso.objects.all()
        # queryset = filter(lambda x: x.credito < 8, iterable)
        # queryset = queryset.filter(credito__lt=8)
        # return queryset.filter(credito__lt=8)
        # return queryset.filter(credito__exact=8)
        # return queryset.filter(nombre__exact='Geografia')
        # return queryset.filter(nombre__contains='ia')
        # return queryset.filter(nombre__startswith='M')
        # return queryset.filter(nombre__endswith='a')
        # return queryset.filter(nombre__iexact='ia')
        # return queryset.filter(credito__range=(3, 8))
        return queryset.order_by('nombre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['title'] = 'Estos son los cursos de la Carrera'
        context['subtitle'] = 'Este es el subtitulo de la materia'
        return context
    
'''
ListView pasa los datos a la plantilla como un diccionario, en este caso:
{
    'title': 'Estos son los cursos de la Carrera',
    'subtitle': 'Este es el subtitulo de la materia',
    'object_list': [lista de objetos del modelo Curso],
}

super().get_queryset() muestra el queryset que hace ListView, osea Curso.objects.all()
context = super().get_context_data(**kwargs) me devuelve el context de ListView, que es un diccionario con la lista del modelo (si no se ha hecho un filtro en get_queryset). En get_context_data, le puedo agregar mas variables
'''


class CursoCreateView(CreateView):
    template_name = "curso_create.html"
    form_class = CursoForm
    success_url = reverse_lazy('cursos:list')

'''
El uso de reverse_lazy garantiza que la URL se resuelva en el momento adecuado y evita problemas con la carga perezosa. Asegúrate de importar reverse_lazy al principio de tu archivo de vistas:
'''

class CursoUpdateView(UpdateView):
    model = Curso
    template_name = "curso_update.html"
    form_class = CursoUpdateForm
    success_url = reverse_lazy('cursos:list')


class CursoDetailView(DetailView):
    model = Curso
    template_name = "curso_detail.html"


class CursoUpdateView(UpdateView):
    model = Curso
    template_name = "curso_update.html"
    form_class = CursoUpdateForm
    success_url = reverse_lazy('cursos:list')

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = "curso_delete.html"
    success_url = reverse_lazy('cursos:list')
