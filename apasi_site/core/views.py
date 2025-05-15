from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContatoForm

def home(request):
    return render(request, 'core/home.html')

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('contato')
        else:
            messages.error(request, 'Por favor, corrija os erros no formulário.')
    else:
        form = ContatoForm()

    return render(request, 'core/contato.html', {'form': form})
