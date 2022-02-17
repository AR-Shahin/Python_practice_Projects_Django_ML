
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from blog.models import Blog, Author


def index(request):
    context = {
        'featured_blogs': Blog.objects.filter(is_featured=True).order_by('-created_at'),
        'blogs': Blog.objects.order_by('-created_at').all(),
    }
    return render(request, 'blog/home.html', context)


def single(request, slug='none'):
    try:
        obj = Blog.objects.get(slug=slug)
        return render(request, 'blog/single.html', {'blog': obj})
    except Blog.DoesNotExist:
        return redirect('blog.index')
