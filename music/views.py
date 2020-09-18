from django.shortcuts import render
from .models import Album, Music, Uploaded_Music

def index(request):

    return HttpResponse("Hello, world. This is a page for index.")


# Create your views here.
