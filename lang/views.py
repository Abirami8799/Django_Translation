from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import get_language, activate,gettext

# Create your views here.

def home(request):
    trans = get_language()
    activate(trans)
    return render(request, 'home.html')

# activate('en')
# activate('hi')
# activate('ta')

       
    
