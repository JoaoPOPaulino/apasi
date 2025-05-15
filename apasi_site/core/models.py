from django.db import models

class Contato(models.Model):
    TIPO_PESSOA_CHOICES = [
        ('Física', 'Pessoa Física'),
        ('Jurídica', 'Pessoa Jurídica'),
    ]

    tipo_pessoa = models.CharField(max_length=10, choices=TIPO_PESSOA_CHOICES)
    nome = models.CharField(max_length=100, null=False)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    cnpj = models.CharField(max_length=18, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=False, null=False)
    rua = models.CharField(max_length=100, blank=False, null=False)
    numero = models.CharField(max_length=10, blank=False, null=False)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=False, null=False)
    cidade = models.CharField(max_length=100, blank=False, null=False)
    estado = models.CharField(max_length=2, blank=False, null=False)
    aceita_politica = models.BooleanField(default=False)
    enviado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.email})"