from django.shortcuts import render
from core.models import *
import random

# Create your views here.

def index(request):
  return render(request, 'index.html', {})

def stop(request):
  return render(request, 'stop.html', {'parar': request.COOKIES.get('parada')})

def play(request):
  questao = random.choice(Questao.objects.all())

  if request.method == "POST":

    if request.POST['resposta'] == request.COOKIES.get('certa'):

      if request.COOKIES.get('proxima') == '1':
        valor = {'acertar': 2000, 'parar': 1000, 'errar': 500}
        response = render(request, 'play.html', {'questao': questao, 'valor': valor})
        response.set_cookie('proxima', 2)

      elif request.COOKIES.get('proxima') == '2':
        valor = {'acertar': 3000, 'parar': 2000, 'errar': 1000}
        response = render(request, 'play.html', {'questao': questao, 'valor': valor})
        response.set_cookie('proxima', 3)

      elif request.COOKIES.get('proxima') == '3':
        valor = {'acertar': 4000, 'parar': 3000, 'errar': 1500}
        response = render(request, 'play.html', {'questao': questao, 'valor': valor})
        response.set_cookie('proxima', 4)

      elif request.COOKIES.get('proxima') == '4':
        valor = {'acertar': 5000, 'parar': 4000, 'errar': 2000}
        response = render(request, 'play.html', {'questao': questao, 'valor': valor})
        response.set_cookie('proxima', 5)

      elif request.COOKIES.get('proxima') == '5':
        valor = {'acertar': 10000, 'parar': 5000, 'errar': 2500}
        response = render(request, 'play.html', {'questao': questao, 'valor': valor})
        response.set_cookie('proxima', 6)

      elif request.COOKIES.get('proxima') == '6':
        valor = {'acertar': 20000, 'parar': 10000, 'errar': 5000}
        response = render(request, 'play.html', {'questao': questao, 'valor': valor})
        response.set_cookie('proxima', 7)

      elif request.COOKIES.get('proxima') == '7':
        valor = {'acertar': 30000, 'parar': 20000, 'errar': 10000}
        response = render(request, 'play.html', {'questao': questao, 'valor': valor})
        response.set_cookie('proxima', 8)

      elif request.COOKIES.get('proxima') == '8':
        valor = {'acertar': 40000, 'parar': 30000, 'errar': 15000}
        response = render(request, 'play.html', {'questao': questao, 'valor': valor})
        response.set_cookie('proxima', 9)

      elif request.COOKIES.get('proxima') == '9':
        valor = {'acertar': 50000, 'parar': 40000, 'errar': 20000}
        response = render(request, 'play.html', {'questao': questao, 'valor': valor})
        response.set_cookie('proxima', 10)

      elif request.COOKIES.get('proxima') == '10':
        valor = {'acertar': 100000, 'parar': 50000, 'errar': 25000}
        response = render(request, 'play.html', {'questao': questao, 'valor': valor})
        response.set_cookie('proxima', 11)

      elif request.COOKIES.get('proxima') == '11':
        valor = {'acertar': 200000, 'parar': 100000, 'errar': 50000}
        response = render(request, 'play.html', {'questao': questao, 'valor': valor})
        response.set_cookie('proxima', 12)

      elif request.COOKIES.get('proxima') == '12':
        valor = {'acertar': 300000, 'parar': 200000, 'errar': 100000}
        response = render(request, 'play.html', {'questao': questao, 'valor': valor})
        response.set_cookie('proxima', 13)

      elif request.COOKIES.get('proxima') == '13':
        valor = {'acertar': 400000, 'parar': 300000, 'errar': 150000}
        response = render(request, 'play.html', {'questao': questao, 'valor': valor})
        response.set_cookie('proxima', 14)

      elif request.COOKIES.get('proxima') == '14':
        valor = {'acertar': 500000, 'parar': 400000, 'errar': 200000}
        response = render(request, 'play.html', {'questao': questao, 'valor': valor})
        response.set_cookie('proxima', 15)

      elif request.COOKIES.get('proxima') == '15':
        valor = {'acertar': 1000000, 'parar': 500000, 'errar': 0}
        response = render(request, 'play.html', {'questao': questao, 'valor': valor})
        response.set_cookie('proxima', 16)

      elif request.COOKIES.get('proxima') == '16':
        valor = {'acertar': 0, 'parar': 0, 'errar': 0}
        response = render(request, 'win.html', {})

      else:
        response = None
        valor = None

      response.set_cookie('certa', questao.correta)
      response.set_cookie('erro', valor['errar'])
      response.set_cookie('parada', valor['parar'])

    else:
      response = render(request, 'error.html', {'valor': request.COOKIES.get('erro')})

  else:
    valor = {'acertar': 1000, 'parar': 0, 'errar': 0}
    response = render(request, 'play.html', {'questao': questao, 'valor': valor})
    response.set_cookie('proxima', 1)
    response.set_cookie('certa', questao.correta)
    response.set_cookie('erro', valor['errar'])
    response.set_cookie('parada', valor['parar'])

  return response