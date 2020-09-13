from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at User index.")

# Create your views here.
