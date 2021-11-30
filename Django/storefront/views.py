from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('Ok')
    data = {'name': 'Shahin', 'title': 'Learn Django'}
    return render(request, 'index.html', data)
