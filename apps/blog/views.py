from django.shortcuts import render, redirect
from about.models import About
from .models import Blog
from .forms import CommentForm

# Create your views here.

def indexView(request):
    about = About.objects.all()
    ctx = {
        'about': about,
    }
    return render(request, 'index.html', ctx)


def blogView(request):
    blog = Blog.objects.all().order_by('-id')
    ctx = {
        'blogs': blog
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
