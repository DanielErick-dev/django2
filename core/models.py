from django.db import models
from stdimage.models import StdImageField
from django.utils import timezone
from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
    criado = models.DateTimeField('data de criação', default=timezone.now)
    modificado = models.DateTimeField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('ativo?', default=True)

    class Meta:
        abstract = True

class Produto(Base):
    nome = models.CharField('nome', max_length=100)
    preco = models.DecimalField('preco', max_digits=8, decimal_places=2, default=0.00)
    estoque = models.IntegerField('estoque', default=0)
    imagem = StdImageField('imagem', upload_to='produtos', variations={'thumb': (124, 124)}, default='static/images/icone_pizza.jpeg')
    slug = models.SlugField('slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome

def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(produto_pre_save, sender=Produto)


class Login(models.Model):
    usuario=models.CharField('usuario',max_length=15)
    email = models.EmailField('e-mail', max_length=20, default='')
    senha=models.CharField('senha',max_length=10)
    confirmacao_senha = models.CharField('confirmacao de senha', max_length=10, default='')
    def __str__(self):
        return self.usuario
        

    