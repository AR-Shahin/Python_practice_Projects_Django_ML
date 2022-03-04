
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from blog.models import Author, Blog


def index(request):
    return redirect('backend.dashboard')
    return render(request, 'backend/layouts/master.html')


def login(request):
    return render(request, 'backend/auth/login.html')


def registration(request):
    return render(request, 'backend/layouts/base.html')


def dashboard(request):
    return render(request, 'backend/dashboard.html')


def authors(request):
    context = {
        'authors': Author.objects.order_by('-created_at').all()
    }
    return render(request, 'backend/author/index.html', context)


def authors_create(request):
    return render(request, 'backend/author/create.html')


def authors_store(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        author = Author(name=name,
                        email=email,
                        slug=name,
                        password=make_password(password))

        author.save()
        return redirect('backend.authors')
