from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def editing(request):
    return render(request, 'editing.html', {})

def maincontent(request):
    return render(request, 'maincontent.html', {})

def annotation(request):
    return render(request, 'annotation.html', {})

def similar(request):
    return render(request, 'similar.html', {})