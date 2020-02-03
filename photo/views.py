from django.shortcuts import rende
from django.http import HttpResponse, Http404
from django.templatetags.static import static
from .models import Images, Location, Category
from django.db.models.query import QuerySet

# Create your views here.
def home(request):
    images = Images.objects.all()
    location = Location.objects.all()
    context = {
        "images":images,
        "location":location,
    }
    return render(request, 'home.html', context)

def images(request, images_id):
    try:
        images = Images.objects.get(id = images_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"gall/gallery.html", {"images":images})
