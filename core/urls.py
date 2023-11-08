from django.urls import path
from .views import produto, index, contato, produtos_salvos, remover_produto,login,criar_conta

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/', produto, name='produto'),
    path('produtos_salvos/', produtos_salvos, name='produtos_salvos'),
    path('remover_produto/', remover_produto, name='remover_produto'),
    path('login/', login, name='login'),
    path('criar_conta', criar_conta, name='criar_conta'),
]