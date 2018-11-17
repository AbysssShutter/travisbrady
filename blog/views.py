from django.shortcuts import render, get_object_or_404
from . import templates

def index(request):
    return render(request, 'blog/index.html', {})

def about(request):
    return render(request, 'blog/about.html', {})

def contacts(reauest):
    return render(request, 'blog/contact.html', {})