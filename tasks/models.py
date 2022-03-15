from django.db import models
from django.contrib.auth import get_user_model

#Create your models here.  hello world

#class criada
class Task(models.Model):
    #agr criamos os campos que serão inseridos na tabela do db

    STATUS = (
        ('solicitado', 'Solicitado'),
        ('Comprado', 'Comprado'),
        ('Aguardando Orçamento', 'Aguardando Orçamento'),
        ('Recebido', 'Recebido'),
    )

    nomeItem = models.CharField("Nome do item: ", max_length=255)
    quantidade = models.IntegerField(blank=True, null=True)
    observação = models.CharField(max_length=255, null=True)
    orçamento01 = models.FileField(upload_to='', blank=True, null=True) #onde o upload irá ficar tem que ser definido no Media_Root (settigns.py do projeto todo) (quando o site tiver no servidor deve se especificar uma outra pasta)
    orçamento02 = models.FileField(upload_to='', blank=True, null=True) 
    orçamento03 = models.FileField(upload_to='', blank=True, null=True)
    status = models.CharField(
        max_length=22, #aqui precisa ficar o nmr máximo de caracteres que o status terá (ou seja colocamos o nmr máximo da maior palavra)
        choices=STATUS,
    )

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) #aqui será armazenado o id do usuário então iremos filtrar as solicitações de cada usuário para que cada usuário veja somente as suas.
    #O comando on_delete=models.CASCADE serve para apagar todos os dados inseridos por um usuário quando este usuário for excluido

    #com esse comando abaixo pegamos a data da solicitação
    created_at = models.DateTimeField(auto_now_add=True)
    # o comando abaixo serve para sempre que alguém alterar o status o db seja atualizado de acordo
    updated_at =models.DateTimeField(auto_now=True)

    #mostrando nome do item no painel admin no lugar de mostrar tasks objects
    def __str__(self) -> str:
        return self.nomeItem

    
