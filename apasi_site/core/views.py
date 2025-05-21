from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .forms import ContatoForm
from django.conf import settings
from django.core.mail import send_mail


def home(request):
    return render(request, 'core/home.html')

@csrf_protect
def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            contato = form.save()

            # Dados do formulário
            nome = contato.nome
            email = contato.email
            telefone = contato.telefone

            # Corpo do e-mail
            corpo_email = (
                f"Novo contato pelo site:\n\n"
                f"Nome: {nome}\n"
                f"E-mail: {email}\n"
                f"Telefone: {telefone}\n\n"
            )

            # Envia o e-mail
            send_mail(
                subject='[Site] Novo Contato Recebido',
                message=corpo_email,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['ambientallix.comercial01@gmail.com'],
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
