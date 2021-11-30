from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    # return HttpResponse("hii main app")
    data = {'title': 'Hello world in Django!!',
            'style': 'text-align:center;margin: 50px 0;color:red'}
    return render(request, 'index.html', data)
