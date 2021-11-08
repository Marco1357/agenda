from django.shortcuts import render

# Create your views here.
from core.models import Evento


def lista_eventos(resquest):
    evento = Evento.objects.all()
    dados = {'eventos':evento}
    return render(resquest, 'agenda.html', dados)
