from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('params/<slug>', views.params, name='params'),
]
