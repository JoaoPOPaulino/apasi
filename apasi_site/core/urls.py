from django.urls import path
from .views import home, contato, canais_atendimento
urlpatterns = [
    path('', home, name='home'),
    path('contato/', contato, name='contato'),
    path('canais-atendimento/', canais_atendimento, name='canais_atendimento')
]