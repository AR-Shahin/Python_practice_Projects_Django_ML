from email.mime import image
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from blog.models import Author, Blog


def blogs(request):
    context = {
        'blogs': Blog.objects.order_by('-created_at').all()
    }
    return render(request, 'backend/blog/index.html', context)


def blogs_create(request):
    return render(request, 'backend/blog/create.html', {
        'authors': Author.objects.all()
    })


def blogs_store(request):
    if request.method == 'POST':
        name = request.POST['name']
        author = request.POST['author']
        description = request.POST['description']
        image = request.FILES.get('image')
        blog = Blog(name=name,

                    slug=name,
                    description=description,
                    image=image
                    )

        blog.save()
        return redirect('backend.blogs')
