from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto, Login

class ContatoForm(forms.Form):
    nome = forms.CharField(label='nome', max_length=100)
    email = forms.CharField(label='e-mail', max_length=100)
    assunto = forms.CharField(label='assunto', max_length=100)
    mensagem = forms.CharField(label='mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nEmail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='E-mail Enviado Pelo Sistema Django 2',
            body=conteudo,
            from_email='contato@seudominio.com.br',
            to=['contato@seudominio.com.br', ],
            headers={f'reply to': {email}}
        )
        mail.send()

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']

class LoginModelForm(forms.ModelForm):
    class Meta:
        model = Login
        fields=['usuario', 'email', 'senha', 'confirmacao_senha']