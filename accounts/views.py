from django.shortcuts import render, redirect
from .form import CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def register_view(request):
    """
    View para registro de usuários
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Fazer login automático após registro
            login(request, user)
            messages.success(request, 'Conta criada com sucesso! Bem-vindo!')
            return redirect('home')
        else:
            # Se o form não for válido, as mensagens de erro serão exibidas automaticamente
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})
    
def login_view(request):
    """
    View para login de usuários
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Validação básica
        if not username or not password:
            messages.error(request, 'Por favor, preencha todos os campos.')
            return render(request, 'login.html')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Bem-vindo de volta, {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Nome de usuário ou senha incorretos.')
    
    return render(request, 'start_login.html')
    
def logout_view(request):
    """
    View para logout de usuários
    """
    logout(request)
    messages.success(request, 'Você foi desconectado com sucesso.')
    return redirect('home')
