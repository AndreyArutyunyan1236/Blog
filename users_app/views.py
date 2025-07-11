from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
def reg(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            messages.success(request, f'Account created for {username}!')
            return redirect()
        
    form = UserCreationForm()
    
    return render(request, 'users_app/reg.html', { 'form': form })

# messages.debug()
# messages.info()
# messages.success()
# messages.warning()
# messages.error()
