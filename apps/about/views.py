from django.shortcuts import render, redirect

from contact.forms import SubscribeForm
from .models import About


# Create your views here.

def aboutView(request):
    subform = SubscribeForm(request.POST or None)
    if subform.is_valid():
        subform.save()
        return redirect('.')
    about = About.objects.all()
    ctx = {
        'about': about,
        'subform': subform
    }
    return render(request, 'about.html', ctx)
