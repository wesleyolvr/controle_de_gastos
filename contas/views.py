from django.shortcuts import render, redirect
from contas.forms import TransacaoForm
from .models import Transacao
import datetime


def home(request):
    data = {}
    data['now'] = datetime.datetime.now()
    return render(request, 'contas/home.html', data)


def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()

    return render(request, 'contas/home.html', data)


def criar(request):
    data = {}
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Listagem')
    data['form'] = form
    return render(request, 'contas/nova.html', data)


def editar(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('Listagem')
    data['form'] = form
    data['transacao'] = transacao
    return render(request, 'contas/nova.html', data)


def deletar(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()

    return redirect('Listagem')
