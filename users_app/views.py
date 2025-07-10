from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def reg(request):
    form = UserCreationForm()
    return render(request, 'users_app/reg.html', { 'form': form })
