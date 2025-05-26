from django.db import models
from django.core.validators import RegexValidator

class Contato(models.Model):
    TIPO_PESSOA_CHOICES = [
        ('Física', 'Pessoa Física'),
        ('Jurídica', 'Pessoa Jurídica'),
    ]

    tipo_pessoa = models.CharField(max_length=10, choices=TIPO_PESSOA_CHOICES, default='Física')
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\(\d{2}\) \d{5}-\d{4}$', 'Telefone deve estar no formato (DD) 00000-0000.')]
    )
    cpf = models.CharField(
        max_length=14,
        blank=True,
        validators=[RegexValidator(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', 'CPF deve estar no formato 000.000.000-00.')]
    )
    cnpj = models.CharField(
        max_length=18,
        blank=True,
        validators=[RegexValidator(r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$', 'CNPJ deve estar no formato 00.000.000/0000-00.')]
    )
    cep = models.CharField(
        max_length=9,
        validators=[RegexValidator(r'^\d{5}-\d{3}$', 'CEP deve estar no formato 00000-000.')]
    )
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    aceita_politica = models.BooleanField(default=False)
    enviado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['enviado_em']),
        ]

    def __str__(self):
        return f"{self.nome} ({self.email})"
    

    class Cidade(models.Model):
        nome = models.CharField(max_length=100)
        estado = models.ForeignKey('Estado', on_delete=models.CASCADE, related_name='cidades')

        class Meta:
            ordering = ['nome']
            unique_together = ['nome', 'estado']

        def __str__(self):
            return f"{self.nome} - {self.estado.sigla}"
    
    class Estado(models.Model):
        nome = models.CharField(max_length=50)
        sigla = models.CharField(max_length=2, unique=True)

        class Meta:
            ordering = ['nome']

        def __str__(self):
            return self.nome