from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def get_util_ip(request):
    if "ip" in request.session:
        ip = request.session["ip"]
    else:
        ip = "0.0.0.0"
    return HttpResponse("%s" % ip)

def set_util_ip(request, ip):
    request.session["ip"] = ip
    return HttpResponse("IP set %s." % ip)
