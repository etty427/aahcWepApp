from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect


# Create your views here.

def index(request):
    
    context = {
        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'home.html',context)