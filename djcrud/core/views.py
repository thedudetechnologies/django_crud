from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from .forms import SignUpForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})



def home(request):
    

    return render(request, "home.html")



