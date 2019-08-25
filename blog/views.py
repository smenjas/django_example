from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        'author': 'Ben',
        'title': 'Blog Post 1',
        'content': '1st post content',
        'date_posted': 'August 20, 2019',
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': '2nd post content',
        'date_posted': 'August 20, 2019',
    },
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
