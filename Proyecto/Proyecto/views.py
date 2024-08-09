from django.http import HttpResponse


def bienvenida(request):
    return HttpResponse("Bienvenido al curso de django")
