from django.shortcuts import render
from .models import Post

def Home(request):
    
    context = {
        'var_posts': Post.objects.all(),
        'title': 'Home',
    }
    
    return render(request, 'blog_app/home.html', context)

def About(request):
    return render(request, 'blog_app/about.html', {
        'title': 'About Us',
    })
