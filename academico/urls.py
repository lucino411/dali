from django.urls import path
from .views import CursoListView, CursoCreateView, CursoUpdateView, CursoDetailView, CursoDeleteView

app_name = 'cursos'

urlpatterns = [
    path('list/', CursoListView.as_view(), name='list'),
    path('create/', CursoCreateView.as_view(), name='create'), 
    path('<int:pk>/', CursoDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', CursoUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', CursoDeleteView.as_view(), name='delete'),
]
