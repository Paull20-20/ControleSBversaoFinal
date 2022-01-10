from django.db import models

# Create your models here.

#class criada
class Task(models.Model):
    #agr criamos os campos que serão inseridos na tabela do db

    STATUS = (
        ('Comprado', 'Comprado'),
        ('Aguardando Orçamento', 'Aguardando Orçamento'),
        ('Recebido', 'Recebido'),
    )

    nomeItem = models.CharField(max_length=255)
    quantidade = models.CharField(max_length=255)
    status = models.CharField(
        max_length=21, #aqui precisa ficar o nmr máximo de caracteres que o status terá (ou seja colocamos o nmr máximo da maior palavra)
        choices=STATUS,
    )

    #com esse comando pegamos a data da solicitação
    created_at = models.DateTimeField(auto_now_add=True)
    # o comando abaixo serve para sempre que alguém alterar o status o db seja atualizado de acordo
    updated_at =models.DateTimeField(auto_now=True)

    #mostrando nome do item no painel admin no lugar de mostrar tasks objects
    def __str__(self) -> str:
        return self.nomeItem

    