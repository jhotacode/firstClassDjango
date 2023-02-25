from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def miPrimerHolaMundo(request):
    return HttpResponse("Hola mamá estoy programando")

def holaMundoHTML(request):
    titulo = "Primera página con Django"
    desarrollador = "Jhonatan"
    lista = [1,2,3]
    return render(request, 'holaMundo.html')
    '''    
    'tituloPrueba': titulo
        'desarrolladorPrueba' : desarrollador
'''
