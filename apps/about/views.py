from django.shortcuts import render
from .models import About


# Create your views here.

def aboutView(request):
    about = About.objects.all()
    ctx = {
        'about': about
    }
    return render(request, 'about.html', ctx)
