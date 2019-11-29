from django.http import HttpResponse, Http404
from .models import Album
from django.template import loader
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    all_obj = Album.objects.all()
    template = loader.get_template("music/index.html")
    cotext = {
        "all_alb" : all_obj
    }
    return HttpResponse(template.render(cotext, request))
    # return render(request, 'music/index.html', cotext)


def details(request, album_id):
    alu = get_object_or_404(Album, pk = album_id)
    return render(request, "music/details.html", {"alb": alu})

