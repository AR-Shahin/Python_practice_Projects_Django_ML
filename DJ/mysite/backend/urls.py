from unicodedata import name
from django.urls import path

from . import views
from . import blogs

urlpatterns = [
    path('', views.index, name='backend.index'),
    path('dashboard', views.dashboard, name='backend.dashboard'),
    path('login', views.login, name='backend.login'),
    path('', views.registration, name='backend.registration'),

    # Author
    path('authors', views.authors, name='backend.authors'),
    path('authors/create', views.authors_create, name='backend.authors.create'),
    path('authors/store', views.authors_store, name='backend.authors.store'),

    # Blog
    path('blogs', blogs.blogs, name='backend.blogs'),
    path('blogs/create', blogs.blogs_create, name='backend.blogs.create'),
    path('blogs/store', blogs.blogs_store, name='backend.blogs.store'),
]
