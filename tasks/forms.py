from django import forms

from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('nome_item', 'quantidade', 'observação')  #campos que queremos que apareça no front end



