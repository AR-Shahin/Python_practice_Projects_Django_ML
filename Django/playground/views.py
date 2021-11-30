from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    data = {'name': 'Shahin', 'nums': [1, 2, 3, 4, 5, 6]}
    return render(request, 'index.html', data)


def about(request):
    pass
