from django.contrib import admin

# Register your models here.

#aqui registramos todo o model que queremos que esteja na área administrativa ou seja o /admin

from .models import Task

admin.site.register(Task)

#feito os comandos acima, o task aparece lá na área admin


