from django.shortcuts import render
from .models import Destination

# Create your views here.
def agri(request):

    
    return render(request, 'agri.html')

