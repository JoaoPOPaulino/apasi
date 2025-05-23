from django.urls import path
from .views import home, contato, canais_atendimento, sobre_nos, licencas, faq, atuacao
urlpatterns = [
    path('', home, name='home'),
    path('contato/', contato, name='contato'),
    path('canais-atendimento/', canais_atendimento, name='canais_atendimento'),
    path('sobre-nos/', sobre_nos, name='sobre_nos'),
    path('licencas/', licencas, name='licencas'),
    path('faq/', faq, name='faq'),
    path('atuacao/', atuacao, name='atuacao'),

]