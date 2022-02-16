from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from crud.models import ToDo


def index(request):
    data = {
        "todos": ToDo.objects.order_by('-created_at').all()
    }
    return render(request, 'crud/index.html', data)


def create(request):
    return render(request, 'crud/create.html')


def store(request):
    if request.method == "POST":
        title = request.POST['title']
        if not title:
            messages.warning(request, 'Field Must Not Be empty!')
            return redirect('crud.create')

        is_active = request.POST['is_active']
        todo = ToDo(title=title, status=is_active)
        todo.save()
        messages.success(request, 'Form submission successful')
        return redirect('crud.index')


def view(request, id):
    todo = ToDo.objects.get(id=id)
    return render(request, 'crud/view.html', {"todo": todo})


def delete(request, id):
    ToDo.objects.get(id=id).delete()
    messages.info(request, 'Data Deleted successful')
    return redirect('crud.index')


def edit(request, id):
    todo = ToDo.objects.get(id=id)
    return render(request, 'crud/edit.html', {"todo": todo})


def update(request, id):
    todo = ToDo.objects.get(id=id)
    todo.title = request.POST['title']
    todo.status = request.POST['is_active']
    todo.save()
    messages.success(request, 'Data Updated successful')

    return redirect('crud.view', id)


def test(request):
    return render(request, 'base.html')
