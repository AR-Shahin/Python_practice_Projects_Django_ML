from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blog.index'),
    path('single/<str:slug>', views.single, name='blog.single')
]
