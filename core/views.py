from django.shortcuts import render
from .forms import ContatoForm, ProdutoModelForm
from django.contrib import messages
from .models import Produto


def index(request):
    return render(request, 'index.html')


def contato(request):
    form = ContatoForm(request.POST or None)
    if str(request.method) == 'POST':

        if form.is_valid():
            nome = form.cleaned_data['nome']
            print(f'nome: {nome}')
            form.send_mail()
            messages.success(request, 'e-mail enviado com sucesso')
            form = ContatoForm()
        else:
            messages.error(request, 'e-mail não foi enviado com sucesso')

    context = {'form': form}
    return render(request, 'contato.html', context)


def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'produto salvo com sucesso')
            form = ProdutoModelForm()
        else:
            messages.error(request, 'erro ao salvar produto')
    else:
        form = ProdutoModelForm()
    context = {
        'form': form
    }
    return render(request, 'produto.html', context)

def remover_produto(request):
    produto = request.POST.get('produto')
    print(produto)
    produto_removido = Produto.objects.get(nome=produto)
    produto_removido.delete()

    context={'produtos': Produto.objects.all()}
    return render(request,'produtos_cadastrados.html', context)
def produtos_salvos(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, 'produtos_cadastrados.html', context)


def login(request):
    return render(request,'login.html')
