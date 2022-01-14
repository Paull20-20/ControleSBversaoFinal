from django import forms

from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('nomeItem', 'quantidade', 'observação')  #campos que queremos que apareça no front end