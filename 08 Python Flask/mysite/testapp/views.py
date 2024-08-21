from django.http import HttpResponse
from django.shortcuts import render

from django.template import loader
from .models import Person


# Create your views here.

#def index(request):
    #return HttpResponse("Hello World")
    #return render(request, 'index.html')
    
def index(request):
  mypersons = Person.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mypersons': mypersons,
  }
  return HttpResponse(template.render(context, request))
