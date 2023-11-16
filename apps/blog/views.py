from django.shortcuts import render, redirect
from about.models import About
from .models import Blog
from .forms import CommentForm
from django.core.paginator import Paginator
from contact.forms import SubscribeForm


# Create your views here.

def indexView(request):
    subform = SubscribeForm(request.POST or None)
    if subform.is_valid():
        subform.save()
        return redirect('.')
    about = About.objects.all()
    blog = Blog.objects.all().order_by('-id')
    ctx = {
        'about': about,
        'blogs': blog,
        'subform': subform
    }
    return render(request, 'index.html', ctx)


def blogView(request):
    b = Blog.objects.all().order_by('-id')
    p = Paginator(b, 1)
    page = request.GET.get('page')
    blog = p.get_page(page)
    subform = SubscribeForm(request.POST or None)
    if subform.is_valid():
        subform.save()
        return redirect('.')
    ctx = {
        'blogs': blog,
        'subform': subform,
    }
    return render(request, 'blog.html', ctx)


def detailView(request, pk):
    blog = Blog.objects.get(id=pk)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        com = form.save(commit=False)
        com.blog = blog
        com.save()
        return redirect('.')
    ctx = {
        'blog': blog,
        'form': form
    }
    return render(request, 'blog-single.html', ctx)
