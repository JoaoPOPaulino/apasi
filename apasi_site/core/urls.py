from django.urls import path
from .views import home, contato
urlpatterns = [
    path('', home, name='home'),
    path('contato/', contato, name='contato'),
]
