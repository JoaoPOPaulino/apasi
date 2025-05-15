from django.contrib import admin
from .models import Contato

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'enviado_em')
    search_fields = ('nome', 'email')
    list_filter = ('enviado_em',)
