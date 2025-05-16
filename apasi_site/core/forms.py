from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = [
            'tipo_pessoa', 'nome', 'email', 'telefone', 'cpf', 'cnpj',
            'cep', 'rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado',
            'aceita_politica'
        ]
        widgets = {
            'tipo_pessoa': forms.Select(attrs={'class': 'form-select'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome completo', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seu@email.com', 'required': True}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(DDD) 00000-0000', 'required': True}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00.000.000/0000-00'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00000-000', 'required': True}),
            'rua': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da rua', 'required': True}),
            'numero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número', 'required': True}),
            'complemento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Complemento'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bairro', 'required': True}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cidade', 'required': True}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UF', 'required': True}),
            'aceita_politica': forms.CheckboxInput(attrs={'class': 'form-check-input', 'required': True}),
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