# from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
from django.template import loader

# Create your views here.
def index(request):
    all_obj = Album.objects.all()
    template = loader.get_template("music/index.html")
    cotext = {
        "all_alb" : all_obj
    }
    return HttpResponse(template.render(cotext, request))




def details(request, album_id):
    return HttpResponse("<h1> Details for Album Id: " + str(album_id) + "</h2>")

