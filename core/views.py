from django.shortcuts import render
from .forms import ContatoForm, ProdutoModelForm, LoginModelForm
from django.contrib import messages
from .models import Produto, Login


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
    lista_de_usuarios = Login.objects.all()
    form=LoginModelForm()
    if str(request.method) == 'POST':
        form=LoginModelForm(request.POST)
        if form.is_valid():
            usuario=form.cleaned_data['usuario']
            senha=form.cleaned_data['senha']
            for usuario_da_lista in lista_de_usuarios:
                if usuario == usuario_da_lista.usuario:
                    if senha == usuario_da_lista.senha:
                        print(f'seja bem vindo {usuario}')
                        break
            else:
                print('você não é bem vindo ou não criou sua conta ainda')                   
            form=LoginModelForm()
    
    context={'form':form}
    return render(request,'login.html',context)
def criar_conta(request):
    form=LoginModelForm()
    if str(request.method) == 'POST':
        form=LoginModelForm(request.POST)
        if form.is_valid():
            usuario=form.cleaned_data['usuario']
            senha=form.cleaned_data['senha']
            try:
                print(f'usuario:{usuario}\nsenha:{senha}')
                form.save()
            except:  
                print(f'ocorreu um erro')         
            form=LoginModelForm()
    
    context={'form':form}
    return render(request,'criar_conta.html',context)
