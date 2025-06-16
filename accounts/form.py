from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class CustomUserCreationForm(UserCreationForm):
    """
    Formulário customizado para criação de usuários
    """
    
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Remove textos de ajuda padrão do Django
        for fieldname in ["username", "password1", "password2"]:
            self.fields[fieldname].help_text = None
        
        # Customiza os widgets para melhor aparência
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Digite seu nome de usuário',
            'autocomplete': 'username'
        })
        
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Digite sua senha',
            'autocomplete': 'new-password'
        })
        
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirme sua senha',
            'autocomplete': 'new-password'
        })
        
        # Customiza as mensagens de erro
        self.fields['username'].error_messages = {
            'required': 'O nome de usuário é obrigatório.',
            'unique': 'Este nome de usuário já está em uso.',
        }
        
        self.fields['password1'].error_messages = {
            'required': 'A senha é obrigatória.',
        }
        
        self.fields['password2'].error_messages = {
            'required': 'A confirmação de senha é obrigatória.',
        }

    def clean_username(self):
        """
        Validação customizada para o username
        """
        username = self.cleaned_data.get('username')
        
        if len(username) < 3:
            raise forms.ValidationError('O nome de usuário deve ter pelo menos 3 caracteres.')
        
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('Este nome de usuário já está em uso.')
        
        return username

    def clean_password2(self):
        """
        Validação customizada para confirmação de senha
        """
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não coincidem.")
        
        return password2
