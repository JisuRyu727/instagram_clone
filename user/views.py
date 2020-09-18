from django.http import HttpResponse
from .models import Account

def detail(request):
    return HttpResponse("Hello, world. You're at User index.")

def index(request):
    return HttpResponse("Hello, world. This is a page for index.")

# Create your views here.
