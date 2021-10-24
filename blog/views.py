from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

# posts = [
#     {
#         'author' : 'Renita Lobo',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'October 23, 2021'
#     },
#     {   
#         'author' : 'Madhu',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'October 26, 2021'
#     },
#     {
#         'author' : 'Prem',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'October 28, 2021'
#     }    
# ]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
    # return HttpResponse("Welcome home")

def about(request):
    return render(request, 'blog/about.html', {'title': "About"})
    # return HttpResponse("Welome to the about")