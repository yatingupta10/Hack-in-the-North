from django.shortcuts import render

def index(request):
    return render(request, 'trainstat/index.html', {})

def contact(request):
    return render(request, 'trainstat/contact.html', {})

def about(request):
    return render(request, 'trainstat/about.html', {})
# Create your views here.
