from django.http import HttpResponse


def index(request):
    return HttpResponse('Rango diz Ola <a href="/rango/about">About</a>')


def about(request):
    return HttpResponse('Rango diz: Aqui e a pagina Sobre <a href="/rango">Index</a>')
