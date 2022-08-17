from django.urls import path
from . import views
urlpatterns = [
    path('', views.test, name='test'),
    path('colaborador/', views.Collaborator, name='colaborador'),
]