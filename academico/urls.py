from django.urls import path
from django.views.generic import RedirectView
from .views import CursoListView, CursoCreateView, CursoUpdateView, CursoDetailView, CursoDeleteView, DashboardView

# app_name = 'cursos'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'), # Sin namespace
    path('list/', CursoListView.as_view(), name='list'),
    path('create/', CursoCreateView.as_view(), name='create'), 
    path('<int:pk>/', CursoDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', CursoUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', CursoDeleteView.as_view(), name='delete'),
    path('exito/', RedirectView.as_view(url='https://chat.openai.com/'), name='exito'),
]

'''
Un uso hipotetico para RedirectView:
Usar varios RedirectView con patrones de URL específicos para enlazar a secciones diferentes de la documentación o recursos externos puede ser válido en algunos casos, pero generalmente no es la forma más escalable o mantenible. Aquí hay algunas consideraciones:
Consolidación: Puedes considerar consolidar todas las redirecciones relacionadas con la documentación de Django en un solo RedirectView y usar un parámetro para indicar la sección específica. Esto hace que tus patrones de URL sean más limpios y evita la duplicación:

path('manual/django/<str:section>/', RedirectView.as_view(url='https://docs.djangoproject.com/{section}/'), name='django_docs'),

En este caso, el parámetro <str:section> se pasa a la URL de destino, y luego puedes usar {section} como un marcador de posición en tu URL.

Uso de Plantillas: Si los enlaces a la documentación están en tu plantilla, también puedes manejar las redirecciones desde el lado del cliente. Esto podría ser más flexible y permitir cambios sin tener que actualizar las URL en tu aplicación.

Enlaces Dinámicos: Si estás creando enlaces dinámicamente en tu aplicación, podrías tener una vista o función que maneje las redirecciones basadas en algún parámetro o lógica específica.

En resumen, tener muchos RedirectView con patrones de URL específicos para diferentes secciones puede volverse complicado y difícil de mantener. Siempre es una buena idea buscar formas de simplificar y estructurar tu código para que sea más fácil de entender y mantener a medida que tu aplicación crece.

'''