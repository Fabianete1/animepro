from django.shortcuts import render
from .models import Usuario



def index_list(request):
    return render(request, 'anime/index.html', {})

def anime_list(request):
    return render(request, 'anime/Anime.html', {}) 

def galeria_list(request):
    return render(request, 'anime/Galeria.html', {}) 

def manga_list(request):
    return render(request, 'anime/Manga.html', {})

def nosotros_list(request):
    return render(request, 'anime/Nosotros.html', {})

def objeto_list(request):
    return render(request, 'anime/Objeto.html', {})

def registro_list(request):
    return render(request, 'anime/Registro.html', {})