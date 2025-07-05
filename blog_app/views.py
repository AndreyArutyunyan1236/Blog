from django.shortcuts import render

posts = [
    {
        'author': 'Andrey',
        'title': 'Title of Andrey\'s post.',
        'date': '05.07.2025',
        'content': 'SOME CONTENT',
    },
    {
        'author': 'Walter',
        'title': 'Title of Walter\'s post.',
        'date': '06.09.2069',
        'content': 'SOME CONTENT',
    }
]

def Home(request):
    
    context = {
        'var_posts': posts,
        'title': 'Home',
    }
    
    return render(request, 'blog_app/home.html', context)

def About(request):
    return render(request, 'blog_app/about.html', {
        'title': 'About Us',
    })
