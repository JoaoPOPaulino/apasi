from django.contrib import admin
from .models import Contato, Estado, Cidade

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'enviado_em')
    search_fields = ('nome', 'email')
    list_filter = ('enviado_em',)

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sigla']
    search_fields = ['nome', 'sigla']

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'estado']
    list_filter = ['estado']
    search_fields = ['nome']