from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .forms import ContatoForm
from django.conf import settings
from django.core.mail import send_mail
from .models import Estado, Cidade
from .serializers import CidadeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


def home(request):
    return render(request, 'core/home.html')

@csrf_protect
def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            contato = form.save()

            nome = contato.nome
            email = contato.email
            telefone = contato.telefone
            tipo_pessoa = contato.tipo_pessoa
            cpf = contato.cpf  # <- Adicionado
            cnpj = contato.cnpj  # <- Adicionado
            cep = contato.cep
            rua = contato.rua
            numero = contato.numero
            complemento = contato.complemento
            bairro = contato.bairro
            cidade = contato.cidade
            estado = contato.estado

            # Corpo do e-mail   
            corpo_email = (
                    f"Olá, equipe Apasi Ambiental!\n\n"
                    f"Um novo contato foi enviado através do site. Seguem os detalhes abaixo:\n\n"
                    f"📌 INFORMAÇÕES DE CONTATO\n"
                    f"• Nome: {nome}\n"
                    f"• E-mail: {email}\n"
                    f"• Telefone: {telefone}\n\n"
                    f"📌 IDENTIFICAÇÃO\n"
                    f"• Tipo de Pessoa: {tipo_pessoa}\n"
                    f"• {'CPF' if tipo_pessoa == 'Física' else 'CNPJ'}: {cpf if tipo_pessoa == 'Física' else cnpj}\n\n"
                    f"📌 ENDEREÇO\n"
                    f"• CEP: {cep}\n"
                    f"• Rua: {rua}, Nº: {numero}, Complemento: {complemento}\n"
                    f"• Bairro: {bairro}\n"
                    f"• Cidade: {cidade} - {estado}\n\n"
                    f"Atenciosamente,\n"
                    f"Site Apasi Ambiental"
                )
            # Envia o e-mail
            send_mail(
                subject='[Apasi Ambiental] Novo Contato Recebido pelo Site',
                message=corpo_email,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['ambientallix.comercial01@gmail.com', 'ambientallix.relacionamentos@gmail.com'],
                fail_silently=False,
            )

            messages.success(request, 'Mensagem enviada com sucesso! Entraremos em contato em breve.')
            return redirect('contato')
        else:
            messages.error(request, 'Por favor, corrija os erros no formulário.')
    else:
        form = ContatoForm()

    return render(request, 'core/contato.html', {'form': form})



def canais_atendimento(request):
    return render(request, 'core/canais_atendimento.html')

def sobre_nos(request):
    return render(request, 'core/sobre_nos.html')

def licencas(request):
    return render(request, 'core/licencas.html')

def faq(request):
    return render(request, 'core/faq.html')

def atuacao(request):
    estados = Estado.objects.all().order_by('nome')
    return render(request, 'core/atuacao.html', {'estados': estados})

@api_view(['GET'])
def city_list(request):
    cidades = Cidade.objects.all()
    serializer = CidadeSerializer(cidades, many=True)
    return Response(serializer.data)
