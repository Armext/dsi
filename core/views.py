from django.shortcuts import render
from portfolio.models import Project
from .models import Persona


# Create your views here.
def home(request):
    persona = Persona.objects.first()
    return render(request, 'home.html', {'persona': persona})

def about(request):
    persona = Persona.objects.first()
    return render(request, 'about.html', {'persona': persona})

def contact(request):
    persona = Persona.objects.first()
    return render(request, 'contact.html', {'persona': persona})


def portfolio(request):
    return render(request, 'portfolio/portfolio.html')

