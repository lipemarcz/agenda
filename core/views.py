from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from core.models import Evento
# Create your views here.

# def index(request):
   #return redirect('/agenda/')
 
def lista_eventos(request):
    usuario = request.user
    if not usuario.is_authenticated:
        return HttpResponse('Usuário não autenticado')
    evento = Evento.objects.all()
    response = {'eventos': evento}
    return render(request, 'agenda.html', response)

def local_evento(request, titulo_evento):
    try:
        evento = Evento.objects.get(titulo=titulo_evento)
        return HttpResponse(f'Evento: {evento.titulo} - Descrição: {evento.descricao} - Data do Evento: {evento.data_evento}')
    except Evento.DoesNotExist:
        raise Http404("Evento não encontrado")