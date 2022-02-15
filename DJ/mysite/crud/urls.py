from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='crud.index'),
    path('/create', views.create, name='crud.create'),
    path('/store', views.store, name='crud.store'),
    path('/view/<int:id>', views.view, name='crud.view'),
    path('/delete/<int:id>', views.delete, name='crud.delete'),
    path('/edit/<int:id>', views.edit, name='crud.edit'),
    path('/update/<int:id>', views.update, name='crud.update'),
]
