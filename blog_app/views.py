from django.shortcuts import render

def Home(request):
    return render(request, "blog_app/home.html")
