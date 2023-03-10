from django.shortcuts import render, redirect
from .models import *
from .forms import Tarefaforms

# Create your views here.

def home(request):
    tarefas = Tarefa.objects.all()
    form = Tarefaforms()

    if request.method == 'POST':
        form = Tarefaforms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tarefas': tarefas, 'form': form}
    return render(request, 'base/home.html', context)



def updateTarefa(request, pk):
    tarefa = Tarefa.objects.get(id=pk)
    form = Tarefaforms(instance=tarefa)

    if request.method == 'POST':
        form = Tarefaforms(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {'tarefa': tarefa, 'form':form}
    return render(request, 'base/update_tf.html', context)

def deleteTarefa(request, pk):
    tarefa = Tarefa.objects.get(id=pk)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('/')
    
    context = {'tarefa': tarefa}
    return render(request, 'base/delete_tf.html', context)
