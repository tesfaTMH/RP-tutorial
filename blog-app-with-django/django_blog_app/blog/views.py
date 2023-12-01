from django.shortcuts import render

# Create your views here.
# dummy data for the posts
posts = [
    {
        'author': 'Abebe',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 12, 2023'
    },
    {
        'author': 'Tesfu',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 11, 2023'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context=context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})