from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
from core.models import Evento


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuario ou senha invalida')
    return redirect('/')


@login_required(login_url='/login/')
def lista_eventos(resquest):
    usuario = resquest.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(resquest, 'agenda.html', dados)
