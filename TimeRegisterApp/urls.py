from django.urls import path
from . import views
urlpatterns = [
    path('colaborador/', views.Collaborator, name='colaborador'),
    path('apontamento/', views.TimeNote, name='apontamento'),
    path('relatorio/', views.TimeReport, name='relatorio'),
    path('banco-de-horas/', views.time_bank, name='banco-de-horas'),
]