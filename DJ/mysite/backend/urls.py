from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='backend.index'),
    path('dashboard', views.dashboard, name='backend.dashboard'),
    path('login', views.login, name='backend.login'),
    path('', views.registration, name='backend.registration'),

    # Author
    path('authors', views.authors, name='backend.authors'),
    path('authors/create', views.authors_create, name='backend.authors.create'),
    path('authors/store', views.authors_store, name='backend.authors.store'),
]
