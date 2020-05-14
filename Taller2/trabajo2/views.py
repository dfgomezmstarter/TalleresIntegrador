from django.shortcuts import  render, HttpResponse
import requests


def measure(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'fecha' in request.GET and 'valor' in request.GET and 'origen' in request.GET and 'codigoSensor'in request.GET and 'observacion'in request.GET:
        #value = request.GET['value']
        fecha = request.GET['fecha']
        valor = request.GET['valor']
        origen = request.GET['origen']
        codigoSensor = request.GET['codigoSensor']
        observacion = request.GET['observacion']
        # Verifica si el value no esta vacio

        # Crea el json para realizar la petición POST al Web Service
        args = {'fecha':fecha,'valor':valor,'origen':origen,'codigoSensor':codigoSensor,'observacion':observacion}
        response = requests.post('http://127.0.0.1:8000/trabajo1/', args)
        # Convierte la respuesta en JSON
        measure_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/trabajo1/')
    # Convierte la respuesta en JSON
    measures = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "trabajo2/home.html", {'measures': measures})