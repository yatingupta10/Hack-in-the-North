from django.shortcuts import render

def index(request):
    return render(request, 'trainstat/index.html', {})
# Create your views here.
