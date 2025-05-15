from django import forms
from .models import Contato
import re

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = [
            'tipo_pessoa', 'nome', 'email', 'telefone', 'cpf', 'cnpj',
            'cep', 'rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado',
            'aceita_politica'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Seu nome completo', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'seu@email.com', 'required': True}),
            'telefone': forms.TextInput(attrs={'placeholder': '(DDD) 00000-0000', 'required': True}),
            'cpf': forms.TextInput(attrs={'placeholder': '000.000.000-00'}),
            'cnpj': forms.TextInput(attrs={'placeholder': '00.000.000/0000-00'}),
            'cep': forms.TextInput(attrs={'placeholder': '00000-000', 'required': True}),
            'rua': forms.TextInput(attrs={'placeholder': 'Nome da rua', 'required': True}),
            'numero': forms.TextInput(attrs={'placeholder': 'Número', 'required': True}),
            'complemento': forms.TextInput(attrs={'placeholder': 'Complemento'}),
            'bairro': forms.TextInput(attrs={'placeholder': 'Bairro', 'required': True}),
            'cidade': forms.TextInput(attrs={'placeholder': 'Cidade', 'required': True}),
            'estado': forms.TextInput(attrs={'placeholder': 'UF', 'required': True}),
        }

    def clean(self):
        cleaned_data = super().clean()
        tipo_pessoa = cleaned_data.get('tipo_pessoa')
        cpf = cleaned_data.get('cpf')
        cnpj = cleaned_data.get('cnpj')

        if tipo_pessoa == 'Física' and not cpf:
            self.add_error('cpf', 'CPF é obrigatório para Pessoa Física.')
        elif tipo_pessoa == 'Jurídica' and not cnpj:
            self.add_error('cnpj', 'CNPJ é obrigatório para Pessoa Jurídica.')

        return cleaned_data

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        if not re.match(r'^\(\d{2}\) \d{5}-\d{4}$', telefone):
            raise forms.ValidationError('Telefone deve estar no formato (DDD) 00000-0000.')
        return telefone

    def clean_cep(self):
        cep = self.cleaned_data['cep']
        if not re.match(r'^\d{5}-\d{3}$', cep):
            raise forms.ValidationError('CEP deve estar no formato 00000-000.')
        return cep

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if self.cleaned_data.get('tipo_pessoa') == 'Física' and not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
            raise forms.ValidationError('CPF deve estar no formato 000.000.000-00.')
        return cpf

    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
        if self.cleaned_data.get('tipo_pessoa') == 'Jurídica' and not re.match(r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$', cnpj):
            raise forms.ValidationError('CNPJ deve estar no formato 00.000.000/0000-00.')
        return cnpj