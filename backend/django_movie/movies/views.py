from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def movieinfo(request):
    return render(request, 'movieinfo.html')


def boockingticket(request):
    return render(request, 'boockingticket.html')
