from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import TaskForm
from django.contrib import messages #serve para criar mensagens a cada ação com interação no banco de dados

from .models import Task

#Aqui criamos uma constante e nela configuramos o que cada url deve fazer

def taskList(request):
    #chamar todas as nossas tasks do db para o template, chamamos o model e o django saberá o que pegar no banco

    tasks_list = Task.objects.all().order_by('-created_at') #pegando todos os objects do banco, ordenando do mais novo para o mais antigo

    
    paginator = Paginator(tasks_list, 5)
    page = request.GET.get('page')

    tasks = paginator.get_page(page)

    return render(request, 'tasks/list.html', {'tasks': tasks}) #renderizando para um arquivo externo dentro da pasta templates, tasks

def taskView(request, id):
    task = get_object_or_404(Task, pk=id) #primary key = id
    return render (request, 'tasks/task.html', {'tasks': task})


def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False) #vai esperar o processo de inserção de dados e esperar até que o user mande salvar
            task.save()
            return redirect('/') #redirecionando pra list.html

    else:
        form = TaskForm() #daqui jogamos ele pro front end
        return render(request, 'tasks/addtask.html', {'form': form})


def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)

        if(form.is_valid()):
            task.save()
            messages.info(request, 'Item editado com sucesso!')
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

    else:
        return render(request, 'tasks/edittask.html', {'form': form, 'task': task})


def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    messages.info(request, 'Item deletado com sucesso!')
    return redirect('/')



def helloWorld(request):
    return HttpResponse('Primeiro Hello world com django!') #passando mensagem direto


def painel(request):
    return render(request, 'tasks/painel.html')


