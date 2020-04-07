from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.<br><a href='characters/'>Characters</a>")
