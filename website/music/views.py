from django.http import HttpResponse, Http404
from .models import Album
from django.template import loader
from django.shortcuts import render

# Create your views here.
def index(request):
    all_obj = Album.objects.all()
    template = loader.get_template("music/index.html")
    cotext = {
        "all_alb" : all_obj
    }
    return HttpResponse(template.render(cotext, request))


def details(request, album_id):
    try:
        alu= Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("_"*10)

    return render(request, "music/details.html", {"alb": alu})

