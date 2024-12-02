from django.shortcuts import render

def index(request):
    return render(request, 'aiapp/index.html')

def info(request):
    return render(request, 'aiapp/info.html')
