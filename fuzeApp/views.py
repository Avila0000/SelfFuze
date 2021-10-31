from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')