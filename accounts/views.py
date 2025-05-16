from django.shortcuts import render, redirect
from .form import CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

"""def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta Criada com Sucesso.')
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
    
def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Nome ou senha incorreta')
    return render(request, 'login.html')
    
def logout_view(request):
    logout(request)
    return redirect('home')"""

def start_view(request):
    return render(request, 'start_login.html')