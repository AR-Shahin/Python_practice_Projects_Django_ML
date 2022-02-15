from django.shortcuts import render

from django.http import HttpResponse
from .models import Question, Choice
from django.utils import timezone


def index(request):
    q = Question(question_text="Code?", pub_date=timezone.now()).save()

    data = Question.objects.all()
    return HttpResponse(data)


def params(request, slug=10):
    return HttpResponse("Params is {}".format(slug))
